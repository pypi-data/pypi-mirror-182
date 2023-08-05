# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsai_grpc_api/protos/image_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from fsai_grpc_api.protos import utils_pb2 as fsai__grpc__api_dot_protos_dot_utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fsai_grpc_api/protos/image_api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$fsai_grpc_api/protos/image_api.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a fsai_grpc_api/protos/utils.proto\"\xa0\x01\n\x05Image\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x1a\n\x08geo_bbox\x18\x05 \x01(\x0b\x32\x08.GeoBbox\x12\x12\n\nfeature_id\x18\x06 \x01(\x05\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"1\n\x18\x46indOrCreateImageRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\"T\n\x19\x46indOrCreateImageResponse\x12 \n\x0b\x63hange_type\x18\x01 \x01(\x0e\x32\x0b.ChangeType\x12\x15\n\x05image\x18\x02 \x01(\x0b\x32\x06.Image\",\n\x13GetImageByIdRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\"O\n\x14GetImageByIdResponse\x12 \n\x0b\x63hange_type\x18\x01 \x01(\x0e\x32\x0b.ChangeType\x12\x15\n\x05image\x18\x02 \x01(\x0b\x32\x06.Image\"0\n\x17GetImageDataByIdRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\"4\n\x18GetImageDataByIdResponse\x12\x18\n\x10image_data_bytes\x18\x01 \x01(\x0c\x32\xde\x01\n\x08ImageApi\x12J\n\x11\x46indOrCreateImage\x12\x19.FindOrCreateImageRequest\x1a\x1a.FindOrCreateImageResponse\x12;\n\x0cGetImageById\x12\x14.GetImageByIdRequest\x1a\x15.GetImageByIdResponse\x12I\n\x10GetImageDataById\x12\x18.GetImageDataByIdRequest\x1a\x19.GetImageDataByIdResponse0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,fsai__grpc__api_dot_protos_dot_utils__pb2.DESCRIPTOR,])




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Image.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Image.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Image.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='Image.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo_bbox', full_name='Image.geo_bbox', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='Image.feature_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Image.created_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=108,
  serialized_end=268,
)


_FINDORCREATEIMAGEREQUEST = _descriptor.Descriptor(
  name='FindOrCreateImageRequest',
  full_name='FindOrCreateImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='FindOrCreateImageRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=270,
  serialized_end=319,
)


_FINDORCREATEIMAGERESPONSE = _descriptor.Descriptor(
  name='FindOrCreateImageResponse',
  full_name='FindOrCreateImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='FindOrCreateImageResponse.change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='FindOrCreateImageResponse.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=321,
  serialized_end=405,
)


_GETIMAGEBYIDREQUEST = _descriptor.Descriptor(
  name='GetImageByIdRequest',
  full_name='GetImageByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='GetImageByIdRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=407,
  serialized_end=451,
)


_GETIMAGEBYIDRESPONSE = _descriptor.Descriptor(
  name='GetImageByIdResponse',
  full_name='GetImageByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='GetImageByIdResponse.change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='GetImageByIdResponse.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=453,
  serialized_end=532,
)


_GETIMAGEDATABYIDREQUEST = _descriptor.Descriptor(
  name='GetImageDataByIdRequest',
  full_name='GetImageDataByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='GetImageDataByIdRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=534,
  serialized_end=582,
)


_GETIMAGEDATABYIDRESPONSE = _descriptor.Descriptor(
  name='GetImageDataByIdResponse',
  full_name='GetImageDataByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_data_bytes', full_name='GetImageDataByIdResponse.image_data_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=584,
  serialized_end=636,
)

_IMAGE.fields_by_name['geo_bbox'].message_type = fsai__grpc__api_dot_protos_dot_utils__pb2._GEOBBOX
_IMAGE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDORCREATEIMAGEREQUEST.fields_by_name['image'].message_type = _IMAGE
_FINDORCREATEIMAGERESPONSE.fields_by_name['change_type'].enum_type = fsai__grpc__api_dot_protos_dot_utils__pb2._CHANGETYPE
_FINDORCREATEIMAGERESPONSE.fields_by_name['image'].message_type = _IMAGE
_GETIMAGEBYIDREQUEST.fields_by_name['image'].message_type = _IMAGE
_GETIMAGEBYIDRESPONSE.fields_by_name['change_type'].enum_type = fsai__grpc__api_dot_protos_dot_utils__pb2._CHANGETYPE
_GETIMAGEBYIDRESPONSE.fields_by_name['image'].message_type = _IMAGE
_GETIMAGEDATABYIDREQUEST.fields_by_name['image'].message_type = _IMAGE
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['FindOrCreateImageRequest'] = _FINDORCREATEIMAGEREQUEST
DESCRIPTOR.message_types_by_name['FindOrCreateImageResponse'] = _FINDORCREATEIMAGERESPONSE
DESCRIPTOR.message_types_by_name['GetImageByIdRequest'] = _GETIMAGEBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetImageByIdResponse'] = _GETIMAGEBYIDRESPONSE
DESCRIPTOR.message_types_by_name['GetImageDataByIdRequest'] = _GETIMAGEDATABYIDREQUEST
DESCRIPTOR.message_types_by_name['GetImageDataByIdResponse'] = _GETIMAGEDATABYIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

FindOrCreateImageRequest = _reflection.GeneratedProtocolMessageType('FindOrCreateImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDORCREATEIMAGEREQUEST,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:FindOrCreateImageRequest)
  })
_sym_db.RegisterMessage(FindOrCreateImageRequest)

FindOrCreateImageResponse = _reflection.GeneratedProtocolMessageType('FindOrCreateImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDORCREATEIMAGERESPONSE,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:FindOrCreateImageResponse)
  })
_sym_db.RegisterMessage(FindOrCreateImageResponse)

GetImageByIdRequest = _reflection.GeneratedProtocolMessageType('GetImageByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEBYIDREQUEST,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:GetImageByIdRequest)
  })
_sym_db.RegisterMessage(GetImageByIdRequest)

GetImageByIdResponse = _reflection.GeneratedProtocolMessageType('GetImageByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEBYIDRESPONSE,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:GetImageByIdResponse)
  })
_sym_db.RegisterMessage(GetImageByIdResponse)

GetImageDataByIdRequest = _reflection.GeneratedProtocolMessageType('GetImageDataByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEDATABYIDREQUEST,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:GetImageDataByIdRequest)
  })
_sym_db.RegisterMessage(GetImageDataByIdRequest)

GetImageDataByIdResponse = _reflection.GeneratedProtocolMessageType('GetImageDataByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEDATABYIDRESPONSE,
  '__module__' : 'fsai_grpc_api.protos.image_api_pb2'
  # @@protoc_insertion_point(class_scope:GetImageDataByIdResponse)
  })
_sym_db.RegisterMessage(GetImageDataByIdResponse)



_IMAGEAPI = _descriptor.ServiceDescriptor(
  name='ImageApi',
  full_name='ImageApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=639,
  serialized_end=861,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindOrCreateImage',
    full_name='ImageApi.FindOrCreateImage',
    index=0,
    containing_service=None,
    input_type=_FINDORCREATEIMAGEREQUEST,
    output_type=_FINDORCREATEIMAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetImageById',
    full_name='ImageApi.GetImageById',
    index=1,
    containing_service=None,
    input_type=_GETIMAGEBYIDREQUEST,
    output_type=_GETIMAGEBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetImageDataById',
    full_name='ImageApi.GetImageDataById',
    index=2,
    containing_service=None,
    input_type=_GETIMAGEDATABYIDREQUEST,
    output_type=_GETIMAGEDATABYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGEAPI)

DESCRIPTOR.services_by_name['ImageApi'] = _IMAGEAPI

# @@protoc_insertion_point(module_scope)
