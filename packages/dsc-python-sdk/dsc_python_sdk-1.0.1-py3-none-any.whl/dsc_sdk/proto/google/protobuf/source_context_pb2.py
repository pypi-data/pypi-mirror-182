# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/source_context.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/source_context.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_options=b'\n\023com.google.protobufB\022SourceContextProtoP\001Z\005types\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$google/protobuf/source_context.proto\x12\x0fgoogle.protobuf\",\n\rSourceContext\x12\x1b\n\tfile_name\x18\x01 \x01(\tR\x08\x66ileNameBY\n\x13\x63om.google.protobufB\x12SourceContextProtoP\x01Z\x05types\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3'
)




_SOURCECONTEXT = _descriptor.Descriptor(
  name='SourceContext',
  full_name='google.protobuf.SourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='google.protobuf.SourceContext.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fileName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=57,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['SourceContext'] = _SOURCECONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SourceContext = _reflection.GeneratedProtocolMessageType('SourceContext', (_message.Message,), {
  'DESCRIPTOR' : _SOURCECONTEXT,
  '__module__' : 'google.protobuf.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.SourceContext)
  })
_sym_db.RegisterMessage(SourceContext)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
