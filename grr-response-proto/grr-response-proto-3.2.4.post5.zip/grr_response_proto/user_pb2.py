# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grr_response_proto/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grr_response_proto import semantic_pb2 as grr__response__proto_dot_semantic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grr_response_proto/user.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1dgrr_response_proto/user.proto\x1a!grr_response_proto/semantic.proto\"\xfd\x01\n\x0bGUISettings\x12\x46\n\x04mode\x18\x01 \x01(\x0e\x32\x13.GUISettings.UIMode:\x05\x42\x41SICB\x1c\xe2\xfc\xe3\xc4\x01\x16\x12\x14User interface mode.\x12L\n\x0b\x63\x61nary_mode\x18\x03 \x01(\x08\x42\x37\xe2\xfc\xe3\xc4\x01\x31\x12/If true, show features that are being canaried.\",\n\x06UIMode\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x0c\n\x08\x41\x44VANCED\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02:*\xda\xfc\xe3\xc4\x01$\n\"User GUI settings and preferences.')
  ,
  dependencies=[grr__response__proto_dot_semantic__pb2.DESCRIPTOR,])



_GUISETTINGS_UIMODE = _descriptor.EnumDescriptor(
  name='UIMode',
  full_name='GUISettings.UIMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BASIC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVANCED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=234,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_GUISETTINGS_UIMODE)


_GUISETTINGS = _descriptor.Descriptor(
  name='GUISettings',
  full_name='GUISettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='GUISettings.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001\026\022\024User interface mode.'))),
    _descriptor.FieldDescriptor(
      name='canary_mode', full_name='GUISettings.canary_mode', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\0011\022/If true, show features that are being canaried.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GUISETTINGS_UIMODE,
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\332\374\343\304\001$\n\"User GUI settings and preferences.')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=322,
)

_GUISETTINGS.fields_by_name['mode'].enum_type = _GUISETTINGS_UIMODE
_GUISETTINGS_UIMODE.containing_type = _GUISETTINGS
DESCRIPTOR.message_types_by_name['GUISettings'] = _GUISETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GUISettings = _reflection.GeneratedProtocolMessageType('GUISettings', (_message.Message,), dict(
  DESCRIPTOR = _GUISETTINGS,
  __module__ = 'grr_response_proto.user_pb2'
  # @@protoc_insertion_point(class_scope:GUISettings)
  ))
_sym_db.RegisterMessage(GUISettings)


_GUISETTINGS.fields_by_name['mode'].has_options = True
_GUISETTINGS.fields_by_name['mode']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001\026\022\024User interface mode.'))
_GUISETTINGS.fields_by_name['canary_mode'].has_options = True
_GUISETTINGS.fields_by_name['canary_mode']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\0011\022/If true, show features that are being canaried.'))
_GUISETTINGS.has_options = True
_GUISETTINGS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\332\374\343\304\001$\n\"User GUI settings and preferences.'))
# @@protoc_insertion_point(module_scope)
