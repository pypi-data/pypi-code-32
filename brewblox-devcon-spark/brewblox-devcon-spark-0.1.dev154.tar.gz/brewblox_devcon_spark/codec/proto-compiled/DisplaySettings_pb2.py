# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DisplaySettings.proto

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
  name='DisplaySettings.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x44isplaySettings.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xf8\x02\n\x0f\x44isplaySettings\x12\x34\n\x07widgets\x18\x01 \x03(\x0b\x32\x1c.blox.DisplaySettings.WidgetB\x05\x92?\x02\x10\x06\x12\x13\n\x04name\x18\x02 \x01(\tB\x05\x92?\x02\x08(\x1a\x91\x02\n\x06Widget\x12\x12\n\x03pos\x18\x01 \x01(\rB\x05\x92?\x02\x38\x08\x12\"\n\x08\x62g_color\x18\x02 \x01(\x0c\x42\x10\x92?\x02\x08\x03\x92?\x02x\x01\x8a\xb5\x18\x02\x38\x01\x12\x13\n\x04name\x18\x03 \x01(\tB\x05\x92?\x02\x08\x10\x12!\n\nTempSensor\x18\n \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x02\x92?\x02\x38\x10H\x00\x12)\n\x12SetpointSensorPair\x18\x0b \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x04\x92?\x02\x38\x10H\x00\x12\"\n\x0b\x41\x63tuatorPwm\x18\x0c \x01(\rB\x0b\x8a\xb5\x18\x02\x18\n\x92?\x02\x38\x10H\x00\x12%\n\x0e\x41\x63tuatorAnalog\x18\r \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x05\x92?\x02\x38\x10H\x00\x12\x1a\n\x03Pid\x18\x0e \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x0b\x92?\x02\x38\x10H\x00\x42\x05\n\x03obj:\x06\x92?\x03H\xba\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_DISPLAYSETTINGS_WIDGET = _descriptor.Descriptor(
  name='Widget',
  full_name='blox.DisplaySettings.Widget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='blox.DisplaySettings.Widget.pos', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bg_color', full_name='blox.DisplaySettings.Widget.bg_color', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\010\003\222?\002x\001\212\265\030\0028\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='blox.DisplaySettings.Widget.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\010\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TempSensor', full_name='blox.DisplaySettings.Widget.TempSensor', index=3,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\002\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SetpointSensorPair', full_name='blox.DisplaySettings.Widget.SetpointSensorPair', index=4,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\004\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ActuatorPwm', full_name='blox.DisplaySettings.Widget.ActuatorPwm', index=5,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\n\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ActuatorAnalog', full_name='blox.DisplaySettings.Widget.ActuatorAnalog', index=6,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\005\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Pid', full_name='blox.DisplaySettings.Widget.Pid', index=7,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\013\222?\0028\020'), file=DESCRIPTOR),
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
      name='obj', full_name='blox.DisplaySettings.Widget.obj',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=157,
  serialized_end=430,
)

_DISPLAYSETTINGS = _descriptor.Descriptor(
  name='DisplaySettings',
  full_name='blox.DisplaySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='widgets', full_name='blox.DisplaySettings.widgets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\020\006'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='blox.DisplaySettings.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\010('), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISPLAYSETTINGS_WIDGET, ],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\272\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=438,
)

_DISPLAYSETTINGS_WIDGET.containing_type = _DISPLAYSETTINGS
_DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj'].fields.append(
  _DISPLAYSETTINGS_WIDGET.fields_by_name['TempSensor'])
_DISPLAYSETTINGS_WIDGET.fields_by_name['TempSensor'].containing_oneof = _DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj']
_DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj'].fields.append(
  _DISPLAYSETTINGS_WIDGET.fields_by_name['SetpointSensorPair'])
_DISPLAYSETTINGS_WIDGET.fields_by_name['SetpointSensorPair'].containing_oneof = _DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj']
_DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj'].fields.append(
  _DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorPwm'])
_DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorPwm'].containing_oneof = _DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj']
_DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj'].fields.append(
  _DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorAnalog'])
_DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorAnalog'].containing_oneof = _DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj']
_DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj'].fields.append(
  _DISPLAYSETTINGS_WIDGET.fields_by_name['Pid'])
_DISPLAYSETTINGS_WIDGET.fields_by_name['Pid'].containing_oneof = _DISPLAYSETTINGS_WIDGET.oneofs_by_name['obj']
_DISPLAYSETTINGS.fields_by_name['widgets'].message_type = _DISPLAYSETTINGS_WIDGET
DESCRIPTOR.message_types_by_name['DisplaySettings'] = _DISPLAYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisplaySettings = _reflection.GeneratedProtocolMessageType('DisplaySettings', (_message.Message,), dict(

  Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), dict(
    DESCRIPTOR = _DISPLAYSETTINGS_WIDGET,
    __module__ = 'DisplaySettings_pb2'
    # @@protoc_insertion_point(class_scope:blox.DisplaySettings.Widget)
    ))
  ,
  DESCRIPTOR = _DISPLAYSETTINGS,
  __module__ = 'DisplaySettings_pb2'
  # @@protoc_insertion_point(class_scope:blox.DisplaySettings)
  ))
_sym_db.RegisterMessage(DisplaySettings)
_sym_db.RegisterMessage(DisplaySettings.Widget)


_DISPLAYSETTINGS_WIDGET.fields_by_name['pos']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['bg_color']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['name']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['TempSensor']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['SetpointSensorPair']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorPwm']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['ActuatorAnalog']._options = None
_DISPLAYSETTINGS_WIDGET.fields_by_name['Pid']._options = None
_DISPLAYSETTINGS.fields_by_name['widgets']._options = None
_DISPLAYSETTINGS.fields_by_name['name']._options = None
_DISPLAYSETTINGS._options = None
# @@protoc_insertion_point(module_scope)
