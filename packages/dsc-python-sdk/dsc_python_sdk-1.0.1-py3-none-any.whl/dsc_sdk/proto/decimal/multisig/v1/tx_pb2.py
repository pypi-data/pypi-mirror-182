# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/multisig/v1/tx.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/multisig/v1/tx.proto',
  package='decimal.multisig.v1',
  syntax='proto3',
  serialized_options=b'\n\027com.decimal.multisig.v1B\007TxProtoP\001Z8bitbucket.org/decimalteam/go-smart-node/x/multisig/types\242\002\003DMX\252\002\023Decimal.Multisig.V1\312\002\023Decimal\\Multisig\\V1\342\002\037Decimal\\Multisig\\V1\\GPBMetadata\352\002\025Decimal::Multisig::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x64\x65\x63imal/multisig/v1/tx.proto\x12\x13\x64\x65\x63imal.multisig.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\xa0\x01\n\x0fMsgCreateWallet\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x16\n\x06owners\x18\x02 \x03(\tR\x06owners\x12\x18\n\x07weights\x18\x03 \x03(\rR\x07weights\x12\x1c\n\tthreshold\x18\x04 \x01(\rR\tthreshold:\x0b\x82\xe7\xb0*\x06sender\"K\n\x17MsgCreateWalletResponse\x12\x30\n\x06wallet\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06wallet\"\xc4\x01\n\x14MsgCreateTransaction\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x30\n\x06wallet\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06wallet\x12;\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07\x43ontentR\x07\x63ontent:\x0b\x82\xe7\xb0*\x06sender\"6\n\x1cMsgCreateTransactionResponse\x12\x16\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02IDR\x02id\"k\n\x12MsgSignTransaction\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x16\n\x02id\x18\x02 \x01(\tB\x06\xe2\xde\x1f\x02IDR\x02id:\x0b\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgSignTransactionResponse2\xc9\x02\n\x03Msg\x12\x62\n\x0c\x43reateWallet\x12$.decimal.multisig.v1.MsgCreateWallet\x1a,.decimal.multisig.v1.MsgCreateWalletResponse\x12q\n\x11\x43reateTransaction\x12).decimal.multisig.v1.MsgCreateTransaction\x1a\x31.decimal.multisig.v1.MsgCreateTransactionResponse\x12k\n\x0fSignTransaction\x12\'.decimal.multisig.v1.MsgSignTransaction\x1a/.decimal.multisig.v1.MsgSignTransactionResponseB\xca\x01\n\x17\x63om.decimal.multisig.v1B\x07TxProtoP\x01Z8bitbucket.org/decimalteam/go-smart-node/x/multisig/types\xa2\x02\x03\x44MX\xaa\x02\x13\x44\x65\x63imal.Multisig.V1\xca\x02\x13\x44\x65\x63imal\\Multisig\\V1\xe2\x02\x1f\x44\x65\x63imal\\Multisig\\V1\\GPBMetadata\xea\x02\x15\x44\x65\x63imal::Multisig::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_msg_dot_v1_dot_msg__pb2.DESCRIPTOR,])




_MSGCREATEWALLET = _descriptor.Descriptor(
  name='MsgCreateWallet',
  full_name='decimal.multisig.v1.MsgCreateWallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.multisig.v1.MsgCreateWallet.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owners', full_name='decimal.multisig.v1.MsgCreateWallet.owners', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='owners', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weights', full_name='decimal.multisig.v1.MsgCreateWallet.weights', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='weights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='decimal.multisig.v1.MsgCreateWallet.threshold', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='threshold', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\202\347\260*\006sender',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=315,
)


_MSGCREATEWALLETRESPONSE = _descriptor.Descriptor(
  name='MsgCreateWalletResponse',
  full_name='decimal.multisig.v1.MsgCreateWalletResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet', full_name='decimal.multisig.v1.MsgCreateWalletResponse.wallet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='wallet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=317,
  serialized_end=392,
)


_MSGCREATETRANSACTION = _descriptor.Descriptor(
  name='MsgCreateTransaction',
  full_name='decimal.multisig.v1.MsgCreateTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.multisig.v1.MsgCreateTransaction.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wallet', full_name='decimal.multisig.v1.MsgCreateTransaction.wallet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='wallet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='decimal.multisig.v1.MsgCreateTransaction.content', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\007Content', json_name='content', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\202\347\260*\006sender',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=591,
)


_MSGCREATETRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='MsgCreateTransactionResponse',
  full_name='decimal.multisig.v1.MsgCreateTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='decimal.multisig.v1.MsgCreateTransactionResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=593,
  serialized_end=647,
)


_MSGSIGNTRANSACTION = _descriptor.Descriptor(
  name='MsgSignTransaction',
  full_name='decimal.multisig.v1.MsgSignTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.multisig.v1.MsgSignTransaction.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='decimal.multisig.v1.MsgSignTransaction.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\202\347\260*\006sender',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=649,
  serialized_end=756,
)


_MSGSIGNTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='MsgSignTransactionResponse',
  full_name='decimal.multisig.v1.MsgSignTransactionResponse',
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
  serialized_start=758,
  serialized_end=786,
)

_MSGCREATETRANSACTION.fields_by_name['content'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['MsgCreateWallet'] = _MSGCREATEWALLET
DESCRIPTOR.message_types_by_name['MsgCreateWalletResponse'] = _MSGCREATEWALLETRESPONSE
DESCRIPTOR.message_types_by_name['MsgCreateTransaction'] = _MSGCREATETRANSACTION
DESCRIPTOR.message_types_by_name['MsgCreateTransactionResponse'] = _MSGCREATETRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['MsgSignTransaction'] = _MSGSIGNTRANSACTION
DESCRIPTOR.message_types_by_name['MsgSignTransactionResponse'] = _MSGSIGNTRANSACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgCreateWallet = _reflection.GeneratedProtocolMessageType('MsgCreateWallet', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEWALLET,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgCreateWallet)
  })
_sym_db.RegisterMessage(MsgCreateWallet)

MsgCreateWalletResponse = _reflection.GeneratedProtocolMessageType('MsgCreateWalletResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEWALLETRESPONSE,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgCreateWalletResponse)
  })
_sym_db.RegisterMessage(MsgCreateWalletResponse)

MsgCreateTransaction = _reflection.GeneratedProtocolMessageType('MsgCreateTransaction', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATETRANSACTION,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgCreateTransaction)
  })
_sym_db.RegisterMessage(MsgCreateTransaction)

MsgCreateTransactionResponse = _reflection.GeneratedProtocolMessageType('MsgCreateTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATETRANSACTIONRESPONSE,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgCreateTransactionResponse)
  })
_sym_db.RegisterMessage(MsgCreateTransactionResponse)

MsgSignTransaction = _reflection.GeneratedProtocolMessageType('MsgSignTransaction', (_message.Message,), {
  'DESCRIPTOR' : _MSGSIGNTRANSACTION,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgSignTransaction)
  })
_sym_db.RegisterMessage(MsgSignTransaction)

MsgSignTransactionResponse = _reflection.GeneratedProtocolMessageType('MsgSignTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSIGNTRANSACTIONRESPONSE,
  '__module__' : 'decimal.multisig.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.MsgSignTransactionResponse)
  })
_sym_db.RegisterMessage(MsgSignTransactionResponse)


DESCRIPTOR._options = None
_MSGCREATEWALLET.fields_by_name['sender']._options = None
_MSGCREATEWALLET._options = None
_MSGCREATEWALLETRESPONSE.fields_by_name['wallet']._options = None
_MSGCREATETRANSACTION.fields_by_name['sender']._options = None
_MSGCREATETRANSACTION.fields_by_name['wallet']._options = None
_MSGCREATETRANSACTION.fields_by_name['content']._options = None
_MSGCREATETRANSACTION._options = None
_MSGCREATETRANSACTIONRESPONSE.fields_by_name['id']._options = None
_MSGSIGNTRANSACTION.fields_by_name['sender']._options = None
_MSGSIGNTRANSACTION.fields_by_name['id']._options = None
_MSGSIGNTRANSACTION._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='decimal.multisig.v1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=789,
  serialized_end=1118,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateWallet',
    full_name='decimal.multisig.v1.Msg.CreateWallet',
    index=0,
    containing_service=None,
    input_type=_MSGCREATEWALLET,
    output_type=_MSGCREATEWALLETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTransaction',
    full_name='decimal.multisig.v1.Msg.CreateTransaction',
    index=1,
    containing_service=None,
    input_type=_MSGCREATETRANSACTION,
    output_type=_MSGCREATETRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SignTransaction',
    full_name='decimal.multisig.v1.Msg.SignTransaction',
    index=2,
    containing_service=None,
    input_type=_MSGSIGNTRANSACTION,
    output_type=_MSGSIGNTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
