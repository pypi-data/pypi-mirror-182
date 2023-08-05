# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/types/v1/indexer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/types/v1/indexer.proto',
  package='ethermint.types.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.ethermint.types.v1B\014IndexerProtoP\001Z github.com/evmos/ethermint/types\242\002\003ETX\252\002\022Ethermint.Types.V1\312\002\022Ethermint\\Types\\V1\342\002\036Ethermint\\Types\\V1\\GPBMetadata\352\002\024Ethermint::Types::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n ethermint/types/v1/indexer.proto\x12\x12\x65thermint.types.v1\x1a\x14gogoproto/gogo.proto\"\xe5\x01\n\x08TxResult\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x19\n\x08tx_index\x18\x02 \x01(\rR\x07txIndex\x12\x1b\n\tmsg_index\x18\x03 \x01(\rR\x08msgIndex\x12 \n\x0c\x65th_tx_index\x18\x04 \x01(\x05R\nethTxIndex\x12\x16\n\x06\x66\x61iled\x18\x05 \x01(\x08R\x06\x66\x61iled\x12\x19\n\x08gas_used\x18\x06 \x01(\x04R\x07gasUsed\x12.\n\x13\x63umulative_gas_used\x18\x07 \x01(\x04R\x11\x63umulativeGasUsed:\x04\x88\xa0\x1f\x00\x42\xb2\x01\n\x16\x63om.ethermint.types.v1B\x0cIndexerProtoP\x01Z github.com/evmos/ethermint/types\xa2\x02\x03\x45TX\xaa\x02\x12\x45thermint.Types.V1\xca\x02\x12\x45thermint\\Types\\V1\xe2\x02\x1e\x45thermint\\Types\\V1\\GPBMetadata\xea\x02\x14\x45thermint::Types::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_TXRESULT = _descriptor.Descriptor(
  name='TxResult',
  full_name='ethermint.types.v1.TxResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='ethermint.types.v1.TxResult.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='height', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_index', full_name='ethermint.types.v1.TxResult.tx_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='txIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_index', full_name='ethermint.types.v1.TxResult.msg_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msgIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eth_tx_index', full_name='ethermint.types.v1.TxResult.eth_tx_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ethTxIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failed', full_name='ethermint.types.v1.TxResult.failed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='failed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='ethermint.types.v1.TxResult.gas_used', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gasUsed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cumulative_gas_used', full_name='ethermint.types.v1.TxResult.cumulative_gas_used', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cumulativeGasUsed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=308,
)

DESCRIPTOR.message_types_by_name['TxResult'] = _TXRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TxResult = _reflection.GeneratedProtocolMessageType('TxResult', (_message.Message,), {
  'DESCRIPTOR' : _TXRESULT,
  '__module__' : 'ethermint.types.v1.indexer_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.types.v1.TxResult)
  })
_sym_db.RegisterMessage(TxResult)


DESCRIPTOR._options = None
_TXRESULT._options = None
# @@protoc_insertion_point(module_scope)
