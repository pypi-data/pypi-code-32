# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stellarstation/api/v1/radio/radio.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stellarstation/api/v1/radio/radio.proto',
  package='stellarstation.api.v1.radio',
  syntax='proto3',
  serialized_options=_b('\n\037com.stellarstation.api.v1.radioB\nRadioProtoP\001Z8github.com/infostellarinc/go-stellarstation/api/v1/radio'),
  serialized_pb=_b('\n\'stellarstation/api/v1/radio/radio.proto\x12\x1bstellarstation.api.v1.radio\"\xcb\x01\n\x18RadioDeviceConfiguration\x12\x1b\n\x13\x63\x65nter_frequency_hz\x18\x01 \x01(\x04\x12;\n\nmodulation\x18\x02 \x01(\x0e\x32\'.stellarstation.api.v1.radio.Modulation\x12\x0f\n\x07\x62itrate\x18\x03 \x01(\x04\x12\x44\n\x08protocol\x18\x04 \x01(\x0b\x32\x32.stellarstation.api.v1.radio.CommunicationProtocol\"U\n\x15\x43ommunicationProtocol\x12\x31\n\x04\x61x25\x18\x01 \x01(\x0b\x32!.stellarstation.api.v1.radio.AX25H\x00\x42\t\n\x07\x46raming\"\x0b\n\tBitStream\"{\n\x04\x41X25\x12\r\n\x05g3ruh\x18\x01 \x01(\x08\x12\x1c\n\x14\x64\x65stination_callsign\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_ssid\x18\x03 \x01(\r\x12\x17\n\x0fsource_callsign\x18\x04 \x01(\t\x12\x13\n\x0bsource_ssid\x18\x05 \x01(\r\"P\n\x19\x43onvolutionalCodingParams\x12\t\n\x01k\x18\x01 \x01(\r\x12\x14\n\x0cinverse_rate\x18\x02 \x01(\r\x12\x12\n\npolynomial\x18\x03 \x03(\x0c\"\xac\x01\n\x10ScramblingParams\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.stellarstation.api.v1.radio.ScramblingParams.Type\x12\x10\n\x08num_bits\x18\x02 \x01(\r\x12\x0c\n\x04mask\x18\x03 \x01(\x0c\x12\x0c\n\x04seed\x18\x04 \x01(\x0c\"(\n\x04Type\x12\x0c\n\x08\x41\x44\x44ITIVE\x10\x00\x12\x12\n\x0eMULTIPLICATIVE\x10\x01*\x87\x02\n\nModulation\x12\x0c\n\x08\x44ISABLED\x10\x00\x12\x07\n\x03\x46SK\x10\x01\x12\x08\n\x04\x41\x46SK\x10\x02\x12\x08\n\x04\x42PSK\x10\x03\x12\x08\n\x04MFSK\x10\x04\x12\x08\n\x04QPSK\x10\x05\x12\x08\n\x04PSK8\x10\x06\x12\t\n\x05PSK16\x10\x07\x12\t\n\x05PSK32\x10\x08\x12\t\n\x05PSK64\x10\t\x12\n\n\x06PSK128\x10\n\x12\n\n\x06PSK256\x10\x0b\x12\t\n\x05OQPSK\x10\x0c\x12\x08\n\x04QAM8\x10\r\x12\t\n\x05QAM16\x10\x0e\x12\t\n\x05QAM32\x10\x0f\x12\t\n\x05QAM64\x10\x10\x12\n\n\x06QAM128\x10\x11\x12\n\n\x06QAM256\x10\x12\x12\x07\n\x03MSK\x10\x13\x12\x08\n\x04GMSK\x10\x14\x12\x06\n\x02\x41M\x10\x15\x12\x06\n\x02\x46M\x10\x16\x12\x06\n\x02PM\x10\x17*S\n\nLineCoding\x12\t\n\x05NRZ_L\x10\x00\x12\t\n\x05NRZ_M\x10\x01\x12\t\n\x05NRZ_S\x10\x02\x12\x06\n\x02RZ\x10\x03\x12\x08\n\x04\x42P_L\x10\x04\x12\x08\n\x04\x42P_M\x10\x05\x12\x08\n\x04\x42P_S\x10\x06\x42i\n\x1f\x63om.stellarstation.api.v1.radioB\nRadioProtoP\x01Z8github.com/infostellarinc/go-stellarstation/api/v1/radiob\x06proto3')
)

_MODULATION = _descriptor.EnumDescriptor(
  name='Modulation',
  full_name='stellarstation.api.v1.radio.Modulation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FSK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFSK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BPSK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MFSK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QPSK', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK8', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK16', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK32', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK64', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK128', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSK256', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OQPSK', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM8', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM16', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM32', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM64', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM128', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QAM256', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSK', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GMSK', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AM', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FM', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PM', index=23, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=761,
  serialized_end=1024,
)
_sym_db.RegisterEnumDescriptor(_MODULATION)

Modulation = enum_type_wrapper.EnumTypeWrapper(_MODULATION)
_LINECODING = _descriptor.EnumDescriptor(
  name='LineCoding',
  full_name='stellarstation.api.v1.radio.LineCoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NRZ_L', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NRZ_M', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NRZ_S', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RZ', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BP_L', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BP_M', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BP_S', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1026,
  serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_LINECODING)

LineCoding = enum_type_wrapper.EnumTypeWrapper(_LINECODING)
DISABLED = 0
FSK = 1
AFSK = 2
BPSK = 3
MFSK = 4
QPSK = 5
PSK8 = 6
PSK16 = 7
PSK32 = 8
PSK64 = 9
PSK128 = 10
PSK256 = 11
OQPSK = 12
QAM8 = 13
QAM16 = 14
QAM32 = 15
QAM64 = 16
QAM128 = 17
QAM256 = 18
MSK = 19
GMSK = 20
AM = 21
FM = 22
PM = 23
NRZ_L = 0
NRZ_M = 1
NRZ_S = 2
RZ = 3
BP_L = 4
BP_M = 5
BP_S = 6


_SCRAMBLINGPARAMS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='stellarstation.api.v1.radio.ScramblingParams.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDITIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLICATIVE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=718,
  serialized_end=758,
)
_sym_db.RegisterEnumDescriptor(_SCRAMBLINGPARAMS_TYPE)


_RADIODEVICECONFIGURATION = _descriptor.Descriptor(
  name='RadioDeviceConfiguration',
  full_name='stellarstation.api.v1.radio.RadioDeviceConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='center_frequency_hz', full_name='stellarstation.api.v1.radio.RadioDeviceConfiguration.center_frequency_hz', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modulation', full_name='stellarstation.api.v1.radio.RadioDeviceConfiguration.modulation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitrate', full_name='stellarstation.api.v1.radio.RadioDeviceConfiguration.bitrate', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='stellarstation.api.v1.radio.RadioDeviceConfiguration.protocol', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=276,
)


_COMMUNICATIONPROTOCOL = _descriptor.Descriptor(
  name='CommunicationProtocol',
  full_name='stellarstation.api.v1.radio.CommunicationProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ax25', full_name='stellarstation.api.v1.radio.CommunicationProtocol.ax25', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Framing', full_name='stellarstation.api.v1.radio.CommunicationProtocol.Framing',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=278,
  serialized_end=363,
)


_BITSTREAM = _descriptor.Descriptor(
  name='BitStream',
  full_name='stellarstation.api.v1.radio.BitStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=376,
)


_AX25 = _descriptor.Descriptor(
  name='AX25',
  full_name='stellarstation.api.v1.radio.AX25',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='g3ruh', full_name='stellarstation.api.v1.radio.AX25.g3ruh', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_callsign', full_name='stellarstation.api.v1.radio.AX25.destination_callsign', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_ssid', full_name='stellarstation.api.v1.radio.AX25.destination_ssid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_callsign', full_name='stellarstation.api.v1.radio.AX25.source_callsign', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_ssid', full_name='stellarstation.api.v1.radio.AX25.source_ssid', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=501,
)


_CONVOLUTIONALCODINGPARAMS = _descriptor.Descriptor(
  name='ConvolutionalCodingParams',
  full_name='stellarstation.api.v1.radio.ConvolutionalCodingParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='stellarstation.api.v1.radio.ConvolutionalCodingParams.k', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inverse_rate', full_name='stellarstation.api.v1.radio.ConvolutionalCodingParams.inverse_rate', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polynomial', full_name='stellarstation.api.v1.radio.ConvolutionalCodingParams.polynomial', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=583,
)


_SCRAMBLINGPARAMS = _descriptor.Descriptor(
  name='ScramblingParams',
  full_name='stellarstation.api.v1.radio.ScramblingParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='stellarstation.api.v1.radio.ScramblingParams.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_bits', full_name='stellarstation.api.v1.radio.ScramblingParams.num_bits', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='stellarstation.api.v1.radio.ScramblingParams.mask', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed', full_name='stellarstation.api.v1.radio.ScramblingParams.seed', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCRAMBLINGPARAMS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=758,
)

_RADIODEVICECONFIGURATION.fields_by_name['modulation'].enum_type = _MODULATION
_RADIODEVICECONFIGURATION.fields_by_name['protocol'].message_type = _COMMUNICATIONPROTOCOL
_COMMUNICATIONPROTOCOL.fields_by_name['ax25'].message_type = _AX25
_COMMUNICATIONPROTOCOL.oneofs_by_name['Framing'].fields.append(
  _COMMUNICATIONPROTOCOL.fields_by_name['ax25'])
_COMMUNICATIONPROTOCOL.fields_by_name['ax25'].containing_oneof = _COMMUNICATIONPROTOCOL.oneofs_by_name['Framing']
_SCRAMBLINGPARAMS.fields_by_name['type'].enum_type = _SCRAMBLINGPARAMS_TYPE
_SCRAMBLINGPARAMS_TYPE.containing_type = _SCRAMBLINGPARAMS
DESCRIPTOR.message_types_by_name['RadioDeviceConfiguration'] = _RADIODEVICECONFIGURATION
DESCRIPTOR.message_types_by_name['CommunicationProtocol'] = _COMMUNICATIONPROTOCOL
DESCRIPTOR.message_types_by_name['BitStream'] = _BITSTREAM
DESCRIPTOR.message_types_by_name['AX25'] = _AX25
DESCRIPTOR.message_types_by_name['ConvolutionalCodingParams'] = _CONVOLUTIONALCODINGPARAMS
DESCRIPTOR.message_types_by_name['ScramblingParams'] = _SCRAMBLINGPARAMS
DESCRIPTOR.enum_types_by_name['Modulation'] = _MODULATION
DESCRIPTOR.enum_types_by_name['LineCoding'] = _LINECODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RadioDeviceConfiguration = _reflection.GeneratedProtocolMessageType('RadioDeviceConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _RADIODEVICECONFIGURATION,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.RadioDeviceConfiguration)
  ))
_sym_db.RegisterMessage(RadioDeviceConfiguration)

CommunicationProtocol = _reflection.GeneratedProtocolMessageType('CommunicationProtocol', (_message.Message,), dict(
  DESCRIPTOR = _COMMUNICATIONPROTOCOL,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.CommunicationProtocol)
  ))
_sym_db.RegisterMessage(CommunicationProtocol)

BitStream = _reflection.GeneratedProtocolMessageType('BitStream', (_message.Message,), dict(
  DESCRIPTOR = _BITSTREAM,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.BitStream)
  ))
_sym_db.RegisterMessage(BitStream)

AX25 = _reflection.GeneratedProtocolMessageType('AX25', (_message.Message,), dict(
  DESCRIPTOR = _AX25,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.AX25)
  ))
_sym_db.RegisterMessage(AX25)

ConvolutionalCodingParams = _reflection.GeneratedProtocolMessageType('ConvolutionalCodingParams', (_message.Message,), dict(
  DESCRIPTOR = _CONVOLUTIONALCODINGPARAMS,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.ConvolutionalCodingParams)
  ))
_sym_db.RegisterMessage(ConvolutionalCodingParams)

ScramblingParams = _reflection.GeneratedProtocolMessageType('ScramblingParams', (_message.Message,), dict(
  DESCRIPTOR = _SCRAMBLINGPARAMS,
  __module__ = 'stellarstation.api.v1.radio.radio_pb2'
  # @@protoc_insertion_point(class_scope:stellarstation.api.v1.radio.ScramblingParams)
  ))
_sym_db.RegisterMessage(ScramblingParams)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
