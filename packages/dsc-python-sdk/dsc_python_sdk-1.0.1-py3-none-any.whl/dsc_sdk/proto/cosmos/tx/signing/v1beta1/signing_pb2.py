# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/signing/v1beta1/signing.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/tx/signing/v1beta1/signing.proto',
  package='cosmos.tx.signing.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\035com.cosmos.tx.signing.v1beta1B\014SigningProtoP\001Z-github.com/cosmos/cosmos-sdk/types/tx/signing\242\002\003CTS\252\002\031Cosmos.Tx.Signing.V1beta1\312\002\031Cosmos\\Tx\\Signing\\V1beta1\342\002%Cosmos\\Tx\\Signing\\V1beta1\\GPBMetadata\352\002\034Cosmos::Tx::Signing::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'cosmos/tx/signing/v1beta1/signing.proto\x12\x19\x63osmos.tx.signing.v1beta1\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x19google/protobuf/any.proto\"f\n\x14SignatureDescriptors\x12N\n\nsignatures\x18\x01 \x03(\x0b\x32..cosmos.tx.signing.v1beta1.SignatureDescriptorR\nsignatures\"\xf5\x04\n\x13SignatureDescriptor\x12\x33\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\tpublicKey\x12G\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.DataR\x04\x64\x61ta\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\x1a\xc3\x03\n\x04\x44\x61ta\x12T\n\x06single\x18\x01 \x01(\x0b\x32:.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.SingleH\x00R\x06single\x12Q\n\x05multi\x18\x02 \x01(\x0b\x32\x39.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.MultiH\x00R\x05multi\x1a_\n\x06Single\x12\x37\n\x04mode\x18\x01 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignModeR\x04mode\x12\x1c\n\tsignature\x18\x02 \x01(\x0cR\tsignature\x1a\xa9\x01\n\x05Multi\x12K\n\x08\x62itarray\x18\x01 \x01(\x0b\x32/.cosmos.crypto.multisig.v1beta1.CompactBitArrayR\x08\x62itarray\x12S\n\nsignatures\x18\x02 \x03(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.DataR\nsignaturesB\x05\n\x03sum*s\n\x08SignMode\x12\x19\n\x15SIGN_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SIGN_MODE_DIRECT\x10\x01\x12\x15\n\x11SIGN_MODE_TEXTUAL\x10\x02\x12\x1f\n\x1bSIGN_MODE_LEGACY_AMINO_JSON\x10\x7f\x42\xe3\x01\n\x1d\x63om.cosmos.tx.signing.v1beta1B\x0cSigningProtoP\x01Z-github.com/cosmos/cosmos-sdk/types/tx/signing\xa2\x02\x03\x43TS\xaa\x02\x19\x43osmos.Tx.Signing.V1beta1\xca\x02\x19\x43osmos\\Tx\\Signing\\V1beta1\xe2\x02%Cosmos\\Tx\\Signing\\V1beta1\\GPBMetadata\xea\x02\x1c\x43osmos::Tx::Signing::V1beta1b\x06proto3'
  ,
  dependencies=[cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_SIGNMODE = _descriptor.EnumDescriptor(
  name='SignMode',
  full_name='cosmos.tx.signing.v1beta1.SignMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_DIRECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_TEXTUAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_LEGACY_AMINO_JSON', index=3, number=127,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=880,
  serialized_end=995,
)
_sym_db.RegisterEnumDescriptor(_SIGNMODE)

SignMode = enum_type_wrapper.EnumTypeWrapper(_SIGNMODE)
SIGN_MODE_UNSPECIFIED = 0
SIGN_MODE_DIRECT = 1
SIGN_MODE_TEXTUAL = 2
SIGN_MODE_LEGACY_AMINO_JSON = 127



_SIGNATUREDESCRIPTORS = _descriptor.Descriptor(
  name='SignatureDescriptors',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signatures', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptors.signatures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signatures', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=144,
  serialized_end=246,
)


_SIGNATUREDESCRIPTOR_DATA_SINGLE = _descriptor.Descriptor(
  name='Single',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=604,
  serialized_end=699,
)

_SIGNATUREDESCRIPTOR_DATA_MULTI = _descriptor.Descriptor(
  name='Multi',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bitarray', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi.bitarray', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bitarray', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signatures', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=702,
  serialized_end=871,
)

_SIGNATUREDESCRIPTOR_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='single', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.multi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='multi', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDESCRIPTOR_DATA_SINGLE, _SIGNATUREDESCRIPTOR_DATA_MULTI, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sum', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=427,
  serialized_end=878,
)

_SIGNATUREDESCRIPTOR = _descriptor.Descriptor(
  name='SignatureDescriptor',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.public_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='publicKey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.sequence', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sequence', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDESCRIPTOR_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=878,
)

_SIGNATUREDESCRIPTORS.fields_by_name['signatures'].message_type = _SIGNATUREDESCRIPTOR
_SIGNATUREDESCRIPTOR_DATA_SINGLE.fields_by_name['mode'].enum_type = _SIGNMODE
_SIGNATUREDESCRIPTOR_DATA_SINGLE.containing_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA_MULTI.fields_by_name['bitarray'].message_type = cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2._COMPACTBITARRAY
_SIGNATUREDESCRIPTOR_DATA_MULTI.fields_by_name['signatures'].message_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA_MULTI.containing_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'].message_type = _SIGNATUREDESCRIPTOR_DATA_SINGLE
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'].message_type = _SIGNATUREDESCRIPTOR_DATA_MULTI
_SIGNATUREDESCRIPTOR_DATA.containing_type = _SIGNATUREDESCRIPTOR
_SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum'].fields.append(
  _SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'])
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'].containing_oneof = _SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum']
_SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum'].fields.append(
  _SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'])
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'].containing_oneof = _SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum']
_SIGNATUREDESCRIPTOR.fields_by_name['public_key'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SIGNATUREDESCRIPTOR.fields_by_name['data'].message_type = _SIGNATUREDESCRIPTOR_DATA
DESCRIPTOR.message_types_by_name['SignatureDescriptors'] = _SIGNATUREDESCRIPTORS
DESCRIPTOR.message_types_by_name['SignatureDescriptor'] = _SIGNATUREDESCRIPTOR
DESCRIPTOR.enum_types_by_name['SignMode'] = _SIGNMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignatureDescriptors = _reflection.GeneratedProtocolMessageType('SignatureDescriptors', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATUREDESCRIPTORS,
  '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptors)
  })
_sym_db.RegisterMessage(SignatureDescriptors)

SignatureDescriptor = _reflection.GeneratedProtocolMessageType('SignatureDescriptor', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

    'Single' : _reflection.GeneratedProtocolMessageType('Single', (_message.Message,), {
      'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA_SINGLE,
      '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
      # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single)
      })
    ,

    'Multi' : _reflection.GeneratedProtocolMessageType('Multi', (_message.Message,), {
      'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA_MULTI,
      '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
      # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi)
      })
    ,
    'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA,
    '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data)
    })
  ,
  'DESCRIPTOR' : _SIGNATUREDESCRIPTOR,
  '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor)
  })
_sym_db.RegisterMessage(SignatureDescriptor)
_sym_db.RegisterMessage(SignatureDescriptor.Data)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Single)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Multi)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
