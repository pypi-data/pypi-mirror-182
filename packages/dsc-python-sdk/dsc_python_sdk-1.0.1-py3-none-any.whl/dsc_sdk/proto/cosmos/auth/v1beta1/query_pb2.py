# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/query.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/auth/v1beta1/query.proto',
  package='cosmos.auth.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\027com.cosmos.auth.v1beta1B\nQueryProtoP\001Z)github.com/cosmos/cosmos-sdk/x/auth/types\242\002\003CAX\252\002\023Cosmos.Auth.V1beta1\312\002\023Cosmos\\Auth\\V1beta1\342\002\037Cosmos\\Auth\\V1beta1\\GPBMetadata\352\002\025Cosmos::Auth::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63osmos/auth/v1beta1/query.proto\x12\x13\x63osmos.auth.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\x1a\x19\x63osmos_proto/cosmos.proto\"^\n\x14QueryAccountsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa0\x01\n\x15QueryAccountsResponse\x12>\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08\x41\x63\x63ountIR\x08\x61\x63\x63ounts\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"9\n\x13QueryAccountRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"T\n\x14QueryAccountResponse\x12<\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08\x41\x63\x63ountIR\x07\x61\x63\x63ount\"\x14\n\x12QueryParamsRequest\"P\n\x13QueryParamsResponse\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.auth.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params2\xa7\x03\n\x05Query\x12\x88\x01\n\x08\x41\x63\x63ounts\x12).cosmos.auth.v1beta1.QueryAccountsRequest\x1a*.cosmos.auth.v1beta1.QueryAccountsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/auth/v1beta1/accounts\x12\x8f\x01\n\x07\x41\x63\x63ount\x12(.cosmos.auth.v1beta1.QueryAccountRequest\x1a).cosmos.auth.v1beta1.QueryAccountResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/auth/v1beta1/accounts/{address}\x12\x80\x01\n\x06Params\x12\'.cosmos.auth.v1beta1.QueryParamsRequest\x1a(.cosmos.auth.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/auth/v1beta1/paramsB\xbe\x01\n\x17\x63om.cosmos.auth.v1beta1B\nQueryProtoP\x01Z)github.com/cosmos/cosmos-sdk/x/auth/types\xa2\x02\x03\x43\x41X\xaa\x02\x13\x43osmos.Auth.V1beta1\xca\x02\x13\x43osmos\\Auth\\V1beta1\xe2\x02\x1f\x43osmos\\Auth\\V1beta1\\GPBMetadata\xea\x02\x15\x43osmos::Auth::V1beta1b\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_auth_dot_v1beta1_dot_auth__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_QUERYACCOUNTSREQUEST = _descriptor.Descriptor(
  name='QueryAccountsRequest',
  full_name='cosmos.auth.v1beta1.QueryAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.auth.v1beta1.QueryAccountsRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=238,
  serialized_end=332,
)


_QUERYACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='QueryAccountsResponse',
  full_name='cosmos.auth.v1beta1.QueryAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='cosmos.auth.v1beta1.QueryAccountsResponse.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\010AccountI', json_name='accounts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.auth.v1beta1.QueryAccountsResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=335,
  serialized_end=495,
)


_QUERYACCOUNTREQUEST = _descriptor.Descriptor(
  name='QueryAccountRequest',
  full_name='cosmos.auth.v1beta1.QueryAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.auth.v1beta1.QueryAccountRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=554,
)


_QUERYACCOUNTRESPONSE = _descriptor.Descriptor(
  name='QueryAccountResponse',
  full_name='cosmos.auth.v1beta1.QueryAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='cosmos.auth.v1beta1.QueryAccountResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\010AccountI', json_name='account', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=556,
  serialized_end=640,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='cosmos.auth.v1beta1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=642,
  serialized_end=662,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='cosmos.auth.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.auth.v1beta1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=664,
  serialized_end=744,
)

_QUERYACCOUNTSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYACCOUNTSRESPONSE.fields_by_name['accounts'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_QUERYACCOUNTSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYACCOUNTRESPONSE.fields_by_name['account'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = cosmos_dot_auth_dot_v1beta1_dot_auth__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryAccountsRequest'] = _QUERYACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['QueryAccountsResponse'] = _QUERYACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['QueryAccountRequest'] = _QUERYACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['QueryAccountResponse'] = _QUERYACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryAccountsRequest = _reflection.GeneratedProtocolMessageType('QueryAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTSREQUEST,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountsRequest)
  })
_sym_db.RegisterMessage(QueryAccountsRequest)

QueryAccountsResponse = _reflection.GeneratedProtocolMessageType('QueryAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTSRESPONSE,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountsResponse)
  })
_sym_db.RegisterMessage(QueryAccountsResponse)

QueryAccountRequest = _reflection.GeneratedProtocolMessageType('QueryAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTREQUEST,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountRequest)
  })
_sym_db.RegisterMessage(QueryAccountRequest)

QueryAccountResponse = _reflection.GeneratedProtocolMessageType('QueryAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYACCOUNTRESPONSE,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryAccountResponse)
  })
_sym_db.RegisterMessage(QueryAccountResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.auth.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYACCOUNTSRESPONSE.fields_by_name['accounts']._options = None
_QUERYACCOUNTREQUEST._options = None
_QUERYACCOUNTRESPONSE.fields_by_name['account']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.auth.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=747,
  serialized_end=1170,
  methods=[
  _descriptor.MethodDescriptor(
    name='Accounts',
    full_name='cosmos.auth.v1beta1.Query.Accounts',
    index=0,
    containing_service=None,
    input_type=_QUERYACCOUNTSREQUEST,
    output_type=_QUERYACCOUNTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\022\035/cosmos/auth/v1beta1/accounts',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Account',
    full_name='cosmos.auth.v1beta1.Query.Account',
    index=1,
    containing_service=None,
    input_type=_QUERYACCOUNTREQUEST,
    output_type=_QUERYACCOUNTRESPONSE,
    serialized_options=b'\202\323\344\223\002)\022\'/cosmos/auth/v1beta1/accounts/{address}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='cosmos.auth.v1beta1.Query.Params',
    index=2,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/cosmos/auth/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
