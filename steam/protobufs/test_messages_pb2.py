# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_messages.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13test_messages.proto\"\xe9\x02\n\x13\x43omplexProtoMessage\x12\x10\n\x08number32\x18\x01 \x01(\r\x12\x10\n\x08number64\x18\x02 \x01(\x04\x12\x15\n\rlist_number32\x18\x03 \x03(\r\x12\x15\n\rlist_number64\x18\x04 \x03(\x04\x12\x33\n\x08messages\x18\x05 \x03(\x0b\x32!.ComplexProtoMessage.InnerMessage\x12\x31\n\x07\x62uffers\x18\x06 \x03(\x0b\x32 .ComplexProtoMessage.InnerBuffer\x1a-\n\x0cInnerMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0f\n\x07numbers\x18\x02 \x03(\r\x1ai\n\x0bInnerBuffer\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x35\n\x05\x66lags\x18\x02 \x03(\x0b\x32&.ComplexProtoMessage.InnerBuffer.Flags\x1a\x15\n\x05\x46lags\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08'
)




_COMPLEXPROTOMESSAGE_INNERMESSAGE = _descriptor.Descriptor(
  name='InnerMessage',
  full_name='ComplexProtoMessage.InnerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ComplexProtoMessage.InnerMessage.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numbers', full_name='ComplexProtoMessage.InnerMessage.numbers', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=278,
)

_COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS = _descriptor.Descriptor(
  name='Flags',
  full_name='ComplexProtoMessage.InnerBuffer.Flags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='ComplexProtoMessage.InnerBuffer.Flags.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=385,
)

_COMPLEXPROTOMESSAGE_INNERBUFFER = _descriptor.Descriptor(
  name='InnerBuffer',
  full_name='ComplexProtoMessage.InnerBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ComplexProtoMessage.InnerBuffer.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flags', full_name='ComplexProtoMessage.InnerBuffer.flags', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=385,
)

_COMPLEXPROTOMESSAGE = _descriptor.Descriptor(
  name='ComplexProtoMessage',
  full_name='ComplexProtoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number32', full_name='ComplexProtoMessage.number32', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number64', full_name='ComplexProtoMessage.number64', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_number32', full_name='ComplexProtoMessage.list_number32', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_number64', full_name='ComplexProtoMessage.list_number64', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messages', full_name='ComplexProtoMessage.messages', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffers', full_name='ComplexProtoMessage.buffers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPLEXPROTOMESSAGE_INNERMESSAGE, _COMPLEXPROTOMESSAGE_INNERBUFFER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=385,
)

_COMPLEXPROTOMESSAGE_INNERMESSAGE.containing_type = _COMPLEXPROTOMESSAGE
_COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS.containing_type = _COMPLEXPROTOMESSAGE_INNERBUFFER
_COMPLEXPROTOMESSAGE_INNERBUFFER.fields_by_name['flags'].message_type = _COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS
_COMPLEXPROTOMESSAGE_INNERBUFFER.containing_type = _COMPLEXPROTOMESSAGE
_COMPLEXPROTOMESSAGE.fields_by_name['messages'].message_type = _COMPLEXPROTOMESSAGE_INNERMESSAGE
_COMPLEXPROTOMESSAGE.fields_by_name['buffers'].message_type = _COMPLEXPROTOMESSAGE_INNERBUFFER
DESCRIPTOR.message_types_by_name['ComplexProtoMessage'] = _COMPLEXPROTOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComplexProtoMessage = _reflection.GeneratedProtocolMessageType('ComplexProtoMessage', (_message.Message,), {

  'InnerMessage' : _reflection.GeneratedProtocolMessageType('InnerMessage', (_message.Message,), {
    'DESCRIPTOR' : _COMPLEXPROTOMESSAGE_INNERMESSAGE,
    '__module__' : 'test_messages_pb2'
    # @@protoc_insertion_point(class_scope:ComplexProtoMessage.InnerMessage)
    })
  ,

  'InnerBuffer' : _reflection.GeneratedProtocolMessageType('InnerBuffer', (_message.Message,), {

    'Flags' : _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), {
      'DESCRIPTOR' : _COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS,
      '__module__' : 'test_messages_pb2'
      # @@protoc_insertion_point(class_scope:ComplexProtoMessage.InnerBuffer.Flags)
      })
    ,
    'DESCRIPTOR' : _COMPLEXPROTOMESSAGE_INNERBUFFER,
    '__module__' : 'test_messages_pb2'
    # @@protoc_insertion_point(class_scope:ComplexProtoMessage.InnerBuffer)
    })
  ,
  'DESCRIPTOR' : _COMPLEXPROTOMESSAGE,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:ComplexProtoMessage)
  })
_sym_db.RegisterMessage(ComplexProtoMessage)
_sym_db.RegisterMessage(ComplexProtoMessage.InnerMessage)
_sym_db.RegisterMessage(ComplexProtoMessage.InnerBuffer)
_sym_db.RegisterMessage(ComplexProtoMessage.InnerBuffer.Flags)


# @@protoc_insertion_point(module_scope)
