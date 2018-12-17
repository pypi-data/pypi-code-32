# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tensor2Tensor encoders for music."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tempfile

from tensor2tensor.data_generators import text_encoder

import magenta
from magenta.music import performance_lib
from magenta.protobuf import music_pb2

CHORD_SYMBOL = music_pb2.NoteSequence.TextAnnotation.CHORD_SYMBOL


class MidiPerformanceEncoder(object):
  """Convert between performance event indices and (filenames of) MIDI files."""

  def __init__(self, steps_per_second, num_velocity_bins, min_pitch, max_pitch,
               add_eos=False):
    """Initialize a MidiPerformanceEncoder object.

    Encodes MIDI using a performance event encoding. Index 0 is unused as it is
    reserved for padding. Index 1 is unused unless `add_eos` is True, in which
    case it is appended to all encoded performances.

    No actual encoder interface is defined in Tensor2Tensor, but this class
    contains the same functions as TextEncoder, ImageEncoder, and AudioEncoder.

    Args:
      steps_per_second: Number of steps per second at which to quantize. Also
          used to determine number of time shift events (up to one second).
      num_velocity_bins: Number of quantized velocity bins to use.
      min_pitch: Minimum MIDI pitch to encode.
      max_pitch: Maximum MIDI pitch to encode (inclusive).
      add_eos: Whether or not to add an EOS event to the end of encoded
          performances.
    """
    self._steps_per_second = steps_per_second
    self._num_velocity_bins = num_velocity_bins
    self._add_eos = add_eos

    self._encoding = magenta.music.PerformanceOneHotEncoding(
        num_velocity_bins=num_velocity_bins,
        max_shift_steps=steps_per_second,
        min_pitch=min_pitch,
        max_pitch=max_pitch)

  @property
  def num_reserved_ids(self):
    return text_encoder.NUM_RESERVED_TOKENS

  def encode_note_sequence(self, ns):
    """Transform a NoteSequence into a list of performance event indices.

    Args:
      ns: NoteSequence proto containing the performance to encode.

    Returns:
      ids: List of performance event indices.
    """
    performance = magenta.music.Performance(
        magenta.music.quantize_note_sequence_absolute(
            ns, self._steps_per_second),
        num_velocity_bins=self._num_velocity_bins)

    ids = [self._encoding.encode_event(event) + self.num_reserved_ids
           for event in performance]
    if self._add_eos:
      ids.append(text_encoder.EOS_ID)

    return ids

  def encode(self, s):
    """Transform a MIDI filename into a list of performance event indices.

    Args:
      s: Path to the MIDI file.

    Returns:
      ids: List of performance event indices.
    """
    if s:
      ns = magenta.music.midi_file_to_sequence_proto(s)
    else:
      ns = music_pb2.NoteSequence()
    return self.encode_note_sequence(ns)

  def decode(self, ids, strip_extraneous=False):
    """Transform a sequence of event indices into a performance MIDI file.

    Args:
      ids: List of performance event indices.
      strip_extraneous: Whether to strip EOS and padding from the end of `ids`.

    Returns:
      Path to the temporary file where the MIDI was saved.
    """
    if strip_extraneous:
      ids = text_encoder.strip_ids(ids, list(range(self.num_reserved_ids)))

    performance = magenta.music.Performance(
        quantized_sequence=None,
        steps_per_second=self._steps_per_second,
        num_velocity_bins=self._num_velocity_bins)
    for i in ids:
      performance.append(self._encoding.decode_event(i - self.num_reserved_ids))

    ns = performance.to_sequence()

    _, tmp_file_path = tempfile.mkstemp('_decode.mid')
    magenta.music.sequence_proto_to_midi_file(ns, tmp_file_path)

    return tmp_file_path

  def decode_list(self, ids):
    """Transform a sequence of event indices into a performance MIDI file.

    Args:
      ids: List of performance event indices.

    Returns:
      Single-element list containing path to the temporary file where the MIDI
      was saved.
    """
    return [self.decode(ids)]

  @property
  def vocab_size(self):
    return self._encoding.num_classes + self.num_reserved_ids


class TextChordsEncoder(object):
  """Convert chord symbol sequences to integer indices."""

  def __init__(self, steps_per_quarter):
    """Initialize a TextChordsEncoder object.

    Encodes chord symbols using a vocabulary of triads. Indices 0 and 1 are
    reserved and unused, and the remaining 48 + 1 indices represent each of 4
    triad types over each of 12 roots, plus "no chord".

    Args:
      steps_per_quarter: Number of steps per quarter at which to quantize.
    """
    self._steps_per_quarter = steps_per_quarter
    self._encoding = magenta.music.TriadChordOneHotEncoding()

  @property
  def num_reserved_ids(self):
    return text_encoder.NUM_RESERVED_TOKENS

  def _encode_chord_symbols(self, chords):
    return [self._encoding.encode_event(chord) + self.num_reserved_ids
            for chord in chords]

  def encode_note_sequence(self, ns):
    """Transform a NoteSequence into a list of chord event indices.

    Args:
      ns: NoteSequence proto containing the chords to encode (as text
          annotations).

    Returns:
      ids: List of chord event indices.
    """
    qns = magenta.music.quantize_note_sequence(ns, self._steps_per_quarter)

    chords = []
    current_chord = magenta.music.NO_CHORD
    current_step = 0
    for ta in sorted(qns.text_annotations, key=lambda ta: ta.time):
      if ta.annotation_type != CHORD_SYMBOL:
        continue
      chords += [current_chord] * (ta.quantized_step - current_step)
      current_chord = ta.text
      current_step = ta.quantized_step
    chords += [current_chord] * (qns.total_quantized_steps - current_step)

    return self._encode_chord_symbols(chords)

  def encode(self, s):
    """Transform a space-delimited chord symbols string into indices.

    Args:
      s: Space delimited string containing a chord symbol sequence, e.g.
          'C C G G Am Am F F'.

    Returns:
      ids: List of encoded chord indices.
    """
    return self._encode_chord_symbols(s.split())

  @property
  def vocab_size(self):
    return self._encoding.num_classes + self.num_reserved_ids


class TextMelodyEncoderBase(object):
  """Convert melody sequences to integer indices, abstract base class."""

  def __init__(self, min_pitch, max_pitch):
    self._encoding = magenta.music.MelodyOneHotEncoding(
        min_note=min_pitch, max_note=max_pitch + 1)

  @property
  def num_reserved_ids(self):
    return text_encoder.NUM_RESERVED_TOKENS

  def _encode_melody_events(self, melody):
    return [self._encoding.encode_event(event) + self.num_reserved_ids
            for event in melody]

  def _quantize_note_sequence(self, ns):
    raise NotImplementedError

  def encode_note_sequence(self, ns):
    """Transform a NoteSequence into a list of melody event indices.

    Args:
      ns: NoteSequence proto containing the melody to encode.

    Returns:
      ids: List of melody event indices.
    """
    qns = self._quantize_note_sequence(ns)

    melody = [magenta.music.MELODY_NO_EVENT] * qns.total_quantized_steps
    for note in sorted(qns.notes, key=lambda note: note.start_time):
      melody[note.quantized_start_step] = note.pitch
      if note.quantized_end_step < qns.total_quantized_steps:
        melody[note.quantized_end_step] = magenta.music.MELODY_NOTE_OFF

    return self._encode_melody_events(melody)

  def encode(self, s):
    """Transform a space-delimited melody string into indices.

    Args:
      s: Space delimited string containing a melody sequence, e.g.
          '60 -2 60 -2 67 -2 67 -2 69 -2 69 -2 67 -2 -2 -1' for the first line
          of Twinkle Twinkle Little Star.

    Returns:
      ids: List of encoded melody event indices.
    """
    return self._encode_melody_events([int(a) for a in s.split()])

  @property
  def vocab_size(self):
    return self._encoding.num_classes + self.num_reserved_ids


class TextMelodyEncoder(TextMelodyEncoderBase):
  """Convert melody sequences (with metric timing) to integer indices."""

  def __init__(self, steps_per_quarter, min_pitch, max_pitch):
    super(TextMelodyEncoder, self).__init__(min_pitch, max_pitch)
    self._steps_per_quarter = steps_per_quarter

  def _quantize_note_sequence(self, ns):
    return magenta.music.quantize_note_sequence(ns, self._steps_per_quarter)


class TextMelodyEncoderAbsolute(TextMelodyEncoderBase):
  """Convert melody sequences (with absolute timing) to integer indices."""

  def __init__(self, steps_per_second, min_pitch, max_pitch):
    super(TextMelodyEncoderAbsolute, self).__init__(min_pitch, max_pitch)
    self._steps_per_second = steps_per_second

  def _quantize_note_sequence(self, ns):
    return magenta.music.quantize_note_sequence_absolute(
        ns, self._steps_per_second)


class CompositeScoreEncoder(object):
  """Convert multi-component score sequences to tuples of integer indices."""

  def __init__(self, encoders):
    self._encoders = encoders

  @property
  def num_reserved_ids(self):
    return text_encoder.NUM_RESERVED_TOKENS

  def encode_note_sequence(self, ns):
    return zip(*[encoder.encode_note_sequence(ns)
                 for encoder in self._encoders])

  def encode(self, s):
    """Transform a MusicXML filename into a list of score event index tuples.

    Args:
      s: Path to the MusicXML file.

    Returns:
      ids: List of score event index tuples.
    """
    if s:
      ns = magenta.music.musicxml_file_to_sequence_proto(s)
    else:
      ns = music_pb2.NoteSequence()
    return self.encode_note_sequence(ns)

  @property
  def vocab_size(self):
    return [encoder.vocab_size for encoder in self._encoders]


class FlattenedTextMelodyEncoderAbsolute(TextMelodyEncoderAbsolute):
  """Encodes a melody that is flattened into only rhythm (with velocity).

  TextMelodyEncoderAbsolute encodes the melody as a sequence of MELODY_NO_EVENT,
  MELODY_NOTE_OFF, and pitch ids. This representation contains no
  MELODY_NOTE_OFF events, and instead of pitch ids, uses velocity-bin ids. To
  take advantage of the MelodyOneHotEncoding, this class passes the velocity bin
  range to the parent __init__ in lieu of min_pitch and max_pitch.
  """

  def __init__(self, steps_per_second, num_velocity_bins):
    self._num_velocity_bins = num_velocity_bins

    super(FlattenedTextMelodyEncoderAbsolute, self).__init__(
        steps_per_second,
        min_pitch=1,
        max_pitch=num_velocity_bins)

  def encode_note_sequence(self, ns):
    """Transform a NoteSequence into a list of melody event indices.

    Args:
      ns: NoteSequence proto containing the melody to encode.

    Returns:
      ids: List of melody event indices.
    """
    qns = self._quantize_note_sequence(ns)

    melody = [magenta.music.MELODY_NO_EVENT] * qns.total_quantized_steps
    for note in sorted(qns.notes, key=lambda note: note.start_time):
      quantized_velocity = performance_lib.velocity_to_bin(
          note.velocity, self._num_velocity_bins)

      melody[note.quantized_start_step] = quantized_velocity

    return self._encode_melody_events(melody)

  def encode(self, s):
    """Transforms melody from a midi_file into a list of melody event indices.

    Args:
      s: Path to a MIDI file.

    Returns:
      ids: List of encoded melody event indices.
    """
    ns = magenta.music.midi_file_to_sequence_proto(s)
    encoded = self.encode_note_sequence(ns)
    return encoded
