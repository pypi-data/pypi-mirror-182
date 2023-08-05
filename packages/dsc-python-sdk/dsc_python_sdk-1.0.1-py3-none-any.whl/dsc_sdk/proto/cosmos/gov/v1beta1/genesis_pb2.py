# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/gov/v1beta1/genesis.proto',
  package='cosmos.gov.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\026com.cosmos.gov.v1beta1B\014GenesisProtoP\001Z(github.com/cosmos/cosmos-sdk/x/gov/types\242\002\003CGX\252\002\022Cosmos.Gov.V1beta1\312\002\022Cosmos\\Gov\\V1beta1\342\002\036Cosmos\\Gov\\V1beta1\\GPBMetadata\352\002\024Cosmos::Gov::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cosmos/gov/v1beta1/genesis.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\"\xe9\x04\n\x0cGenesisState\x12Q\n\x14starting_proposal_id\x18\x01 \x01(\x04\x42\x1f\xf2\xde\x1f\x1byaml:\"starting_proposal_id\"R\x12startingProposalId\x12I\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x10\xc8\xde\x1f\x00\xaa\xdf\x1f\x08\x44\x65positsR\x08\x64\x65posits\x12=\n\x05votes\x18\x03 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\r\xc8\xde\x1f\x00\xaa\xdf\x1f\x05VotesR\x05votes\x12M\n\tproposals\x18\x04 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x11\xc8\xde\x1f\x00\xaa\xdf\x1f\tProposalsR\tproposals\x12g\n\x0e\x64\x65posit_params\x18\x05 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"deposit_params\"R\rdepositParams\x12\x63\n\rvoting_params\x18\x06 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"voting_params\"R\x0cvotingParams\x12_\n\x0ctally_params\x18\x07 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"tally_params\"R\x0btallyParamsB\xba\x01\n\x16\x63om.cosmos.gov.v1beta1B\x0cGenesisProtoP\x01Z(github.com/cosmos/cosmos-sdk/x/gov/types\xa2\x02\x03\x43GX\xaa\x02\x12\x43osmos.Gov.V1beta1\xca\x02\x12\x43osmos\\Gov\\V1beta1\xe2\x02\x1e\x43osmos\\Gov\\V1beta1\\GPBMetadata\xea\x02\x14\x43osmos::Gov::V1beta1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_gov_dot_v1beta1_dot_gov__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.gov.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='starting_proposal_id', full_name='cosmos.gov.v1beta1.GenesisState.starting_proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"starting_proposal_id\"', json_name='startingProposalId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deposits', full_name='cosmos.gov.v1beta1.GenesisState.deposits', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037\010Deposits', json_name='deposits', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='votes', full_name='cosmos.gov.v1beta1.GenesisState.votes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037\005Votes', json_name='votes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposals', full_name='cosmos.gov.v1beta1.GenesisState.proposals', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037\tProposals', json_name='proposals', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deposit_params', full_name='cosmos.gov.v1beta1.GenesisState.deposit_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\025yaml:\"deposit_params\"', json_name='depositParams', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voting_params', full_name='cosmos.gov.v1beta1.GenesisState.voting_params', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\024yaml:\"voting_params\"', json_name='votingParams', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tally_params', full_name='cosmos.gov.v1beta1.GenesisState.tally_params', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\023yaml:\"tally_params\"', json_name='tallyParams', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=109,
  serialized_end=726,
)

_GENESISSTATE.fields_by_name['deposits'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSIT
_GENESISSTATE.fields_by_name['votes'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTE
_GENESISSTATE.fields_by_name['proposals'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._PROPOSAL
_GENESISSTATE.fields_by_name['deposit_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSITPARAMS
_GENESISSTATE.fields_by_name['voting_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTINGPARAMS
_GENESISSTATE.fields_by_name['tally_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._TALLYPARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.gov.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['starting_proposal_id']._options = None
_GENESISSTATE.fields_by_name['deposits']._options = None
_GENESISSTATE.fields_by_name['votes']._options = None
_GENESISSTATE.fields_by_name['proposals']._options = None
_GENESISSTATE.fields_by_name['deposit_params']._options = None
_GENESISSTATE.fields_by_name['voting_params']._options = None
_GENESISSTATE.fields_by_name['tally_params']._options = None
# @@protoc_insertion_point(module_scope)
