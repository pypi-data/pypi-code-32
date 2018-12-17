# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TouchSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TouchSettings.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13TouchSettings.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xe5\x01\n\rTouchSettings\x12\x32\n\ncalibrated\x18\x01 \x01(\x0e\x32\x1e.blox.TouchSettings.Calibrated\x12\x16\n\x07xOffset\x18\x02 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12\x16\n\x07yOffset\x18\x03 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12\x1f\n\x10xBitsPerPixelX16\x18\x04 \x01(\rB\x05\x92?\x02\x38\x10\x12\x1f\n\x10yBitsPerPixelX16\x18\x05 \x01(\rB\x05\x92?\x02\x38\x10\"&\n\nCalibrated\x12\x06\n\x02NO\x10\x00\x12\x07\n\x03YES\x10\x01\x12\x07\n\x03NEW\x10\x02:\x06\x92?\x03H\xb9\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])



_TOUCHSETTINGS_CALIBRATED = _descriptor.EnumDescriptor(
  name='Calibrated',
  full_name='blox.TouchSettings.Calibrated',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_TOUCHSETTINGS_CALIBRATED)


_TOUCHSETTINGS = _descriptor.Descriptor(
  name='TouchSettings',
  full_name='blox.TouchSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibrated', full_name='blox.TouchSettings.calibrated', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xOffset', full_name='blox.TouchSettings.xOffset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yOffset', full_name='blox.TouchSettings.yOffset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xBitsPerPixelX16', full_name='blox.TouchSettings.xBitsPerPixelX16', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yBitsPerPixelX16', full_name='blox.TouchSettings.yBitsPerPixelX16', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOUCHSETTINGS_CALIBRATED,
  ],
  serialized_options=_b('\222?\003H\271\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=289,
)

_TOUCHSETTINGS.fields_by_name['calibrated'].enum_type = _TOUCHSETTINGS_CALIBRATED
_TOUCHSETTINGS_CALIBRATED.containing_type = _TOUCHSETTINGS
DESCRIPTOR.message_types_by_name['TouchSettings'] = _TOUCHSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TouchSettings = _reflection.GeneratedProtocolMessageType('TouchSettings', (_message.Message,), dict(
  DESCRIPTOR = _TOUCHSETTINGS,
  __module__ = 'TouchSettings_pb2'
  # @@protoc_insertion_point(class_scope:blox.TouchSettings)
  ))
_sym_db.RegisterMessage(TouchSettings)


_TOUCHSETTINGS.fields_by_name['xOffset']._options = None
_TOUCHSETTINGS.fields_by_name['yOffset']._options = None
_TOUCHSETTINGS.fields_by_name['xBitsPerPixelX16']._options = None
_TOUCHSETTINGS.fields_by_name['yBitsPerPixelX16']._options = None
_TOUCHSETTINGS._options = None
# @@protoc_insertion_point(module_scope)
