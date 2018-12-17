# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grr_response_proto/config.proto

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
  name='grr_response_proto/config.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1fgrr_response_proto/config.proto\x1a!grr_response_proto/semantic.proto\"M\n!AdminUIClientWarningsConfigOption\x12(\n\x05rules\x18\x01 \x03(\x0b\x32\x19.AdminUIClientWarningRule\"\xb8\x01\n\x18\x41\x64minUIClientWarningRule\x12U\n\x0bwith_labels\x18\x01 \x03(\tB@\xe2\xfc\xe3\xc4\x01:\x12\x38List of client labels that a warning message applies to.\x12\x45\n\x07message\x18\x02 \x01(\tB4\xe2\xfc\xe3\xc4\x01.\x12,Warning message text (may contain markdown).')
  ,
  dependencies=[grr__response__proto_dot_semantic__pb2.DESCRIPTOR,])




_ADMINUICLIENTWARNINGSCONFIGOPTION = _descriptor.Descriptor(
  name='AdminUIClientWarningsConfigOption',
  full_name='AdminUIClientWarningsConfigOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='AdminUIClientWarningsConfigOption.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=147,
)


_ADMINUICLIENTWARNINGRULE = _descriptor.Descriptor(
  name='AdminUIClientWarningRule',
  full_name='AdminUIClientWarningRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='with_labels', full_name='AdminUIClientWarningRule.with_labels', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001:\0228List of client labels that a warning message applies to.'))),
    _descriptor.FieldDescriptor(
      name='message', full_name='AdminUIClientWarningRule.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001.\022,Warning message text (may contain markdown).'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=334,
)

_ADMINUICLIENTWARNINGSCONFIGOPTION.fields_by_name['rules'].message_type = _ADMINUICLIENTWARNINGRULE
DESCRIPTOR.message_types_by_name['AdminUIClientWarningsConfigOption'] = _ADMINUICLIENTWARNINGSCONFIGOPTION
DESCRIPTOR.message_types_by_name['AdminUIClientWarningRule'] = _ADMINUICLIENTWARNINGRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminUIClientWarningsConfigOption = _reflection.GeneratedProtocolMessageType('AdminUIClientWarningsConfigOption', (_message.Message,), dict(
  DESCRIPTOR = _ADMINUICLIENTWARNINGSCONFIGOPTION,
  __module__ = 'grr_response_proto.config_pb2'
  # @@protoc_insertion_point(class_scope:AdminUIClientWarningsConfigOption)
  ))
_sym_db.RegisterMessage(AdminUIClientWarningsConfigOption)

AdminUIClientWarningRule = _reflection.GeneratedProtocolMessageType('AdminUIClientWarningRule', (_message.Message,), dict(
  DESCRIPTOR = _ADMINUICLIENTWARNINGRULE,
  __module__ = 'grr_response_proto.config_pb2'
  # @@protoc_insertion_point(class_scope:AdminUIClientWarningRule)
  ))
_sym_db.RegisterMessage(AdminUIClientWarningRule)


_ADMINUICLIENTWARNINGRULE.fields_by_name['with_labels'].has_options = True
_ADMINUICLIENTWARNINGRULE.fields_by_name['with_labels']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001:\0228List of client labels that a warning message applies to.'))
_ADMINUICLIENTWARNINGRULE.fields_by_name['message'].has_options = True
_ADMINUICLIENTWARNINGRULE.fields_by_name['message']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\374\343\304\001.\022,Warning message text (may contain markdown).'))
# @@protoc_insertion_point(module_scope)
