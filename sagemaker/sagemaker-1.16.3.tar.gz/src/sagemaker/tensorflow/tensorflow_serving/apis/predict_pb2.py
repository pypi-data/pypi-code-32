# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/predict.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from tensorflow_serving.apis import model_pb2 as tensorflow__serving_dot_apis_dot_model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/apis/predict.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=_b('\n%tensorflow_serving/apis/predict.proto\x12\x12tensorflow.serving\x1a&tensorflow/core/framework/tensor.proto\x1a#tensorflow_serving/apis/model.proto\"\xe2\x01\n\x0ePredictRequest\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12>\n\x06inputs\x18\x02 \x03(\x0b\x32..tensorflow.serving.PredictRequest.InputsEntry\x12\x15\n\routput_filter\x18\x03 \x03(\t\x1a\x46\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow.TensorProto:\x02\x38\x01\"\xd0\x01\n\x0fPredictResponse\x12\x31\n\nmodel_spec\x18\x02 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12\x41\n\x07outputs\x18\x01 \x03(\x0b\x32\x30.tensorflow.serving.PredictResponse.OutputsEntry\x1aG\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow.TensorProto:\x02\x38\x01\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_model__pb2.DESCRIPTOR,])




_PREDICTREQUEST_INPUTSENTRY = _descriptor.Descriptor(
  name='InputsEntry',
  full_name='tensorflow.serving.PredictRequest.InputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.serving.PredictRequest.InputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.PredictRequest.InputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=365,
)

_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='tensorflow.serving.PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.PredictRequest.model_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tensorflow.serving.PredictRequest.inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_filter', full_name='tensorflow.serving.PredictRequest.output_filter', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTREQUEST_INPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=365,
)


_PREDICTRESPONSE_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='tensorflow.serving.PredictResponse.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.serving.PredictResponse.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.PredictResponse.OutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=576,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='tensorflow.serving.PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.PredictResponse.model_spec', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tensorflow.serving.PredictResponse.outputs', index=1,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_OUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=576,
)

_PREDICTREQUEST_INPUTSENTRY.fields_by_name['value'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_PREDICTREQUEST_INPUTSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name['model_spec'].message_type = tensorflow__serving_dot_apis_dot_model__pb2._MODELSPEC
_PREDICTREQUEST.fields_by_name['inputs'].message_type = _PREDICTREQUEST_INPUTSENTRY
_PREDICTRESPONSE_OUTPUTSENTRY.fields_by_name['value'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_PREDICTRESPONSE_OUTPUTSENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name['model_spec'].message_type = tensorflow__serving_dot_apis_dot_model__pb2._MODELSPEC
_PREDICTRESPONSE.fields_by_name['outputs'].message_type = _PREDICTRESPONSE_OUTPUTSENTRY
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), dict(

  InputsEntry = _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTREQUEST_INPUTSENTRY,
    __module__ = 'tensorflow_serving.apis.predict_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictRequest.InputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTREQUEST,
  __module__ = 'tensorflow_serving.apis.predict_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictRequest)
  ))
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.InputsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), dict(

  OutputsEntry = _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTRESPONSE_OUTPUTSENTRY,
    __module__ = 'tensorflow_serving.apis.predict_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictResponse.OutputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTRESPONSE,
  __module__ = 'tensorflow_serving.apis.predict_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictResponse)
  ))
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.OutputsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
_PREDICTREQUEST_INPUTSENTRY.has_options = True
_PREDICTREQUEST_INPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PREDICTRESPONSE_OUTPUTSENTRY.has_options = True
_PREDICTRESPONSE_OUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
