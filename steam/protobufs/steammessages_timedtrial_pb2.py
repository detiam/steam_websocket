# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_timedtrial.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_timedtrial.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1esteammessages_timedtrial.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"5\n$CTimedTrial_GetTimeRemaining_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\x84\x01\n%CTimedTrial_GetTimeRemaining_Response\x12\x16\n\x0eseconds_played\x18\x01 \x01(\r\x12\x17\n\x0fseconds_allowed\x18\x02 \x01(\r\x12\x11\n\tpackageid\x18\x03 \x01(\r\x12\x17\n\x0fmastersub_appid\x18\x04 \x01(\r\"K\n\"CTimedTrial_RecordPlaytime_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x16\n\x0eseconds_played\x18\x02 \x01(\r\"V\n#CTimedTrial_RecordPlaytime_Response\x12\x16\n\x0eseconds_played\x18\x01 \x01(\r\x12\x17\n\x0fseconds_allowed\x18\x02 \x01(\r\"2\n!CTimedTrial_ResetPlaytime_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"U\n\"CTimedTrial_ResetPlaytime_Response\x12\x16\n\x0eseconds_played\x18\x01 \x01(\r\x12\x17\n\x0fseconds_allowed\x18\x02 \x01(\r2\x9b\x04\n\nTimedTrial\x12\xad\x01\n\x10GetTimeRemaining\x12%.CTimedTrial_GetTimeRemaining_Request\x1a&.CTimedTrial_GetTimeRemaining_Response\"J\x82\xb5\x18\x46Returns the amount of time a user has left on a timed trial for an app\x12\x94\x01\n\x0eRecordPlaytime\x12#.CTimedTrial_RecordPlaytime_Request\x1a$.CTimedTrial_RecordPlaytime_Response\"7\x82\xb5\x18\x33Updates the user\'s remaining playtime while in game\x12\x92\x01\n\rResetPlaytime\x12\".CTimedTrial_ResetPlaytime_Request\x1a#.CTimedTrial_ResetPlaytime_Response\"8\x82\xb5\x18\x34Reset the user\'s remaining playtime (developer only)\x1a\x31\x82\xb5\x18-A service to get user timed trial informationB\x03\x90\x01\x01'
  ,
  dependencies=[steammessages__base__pb2.DESCRIPTOR,steammessages__unified__base__pb2.DESCRIPTOR,])




_CTIMEDTRIAL_GETTIMEREMAINING_REQUEST = _descriptor.Descriptor(
  name='CTimedTrial_GetTimeRemaining_Request',
  full_name='CTimedTrial_GetTimeRemaining_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CTimedTrial_GetTimeRemaining_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=94,
  serialized_end=147,
)


_CTIMEDTRIAL_GETTIMEREMAINING_RESPONSE = _descriptor.Descriptor(
  name='CTimedTrial_GetTimeRemaining_Response',
  full_name='CTimedTrial_GetTimeRemaining_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds_played', full_name='CTimedTrial_GetTimeRemaining_Response.seconds_played', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds_allowed', full_name='CTimedTrial_GetTimeRemaining_Response.seconds_allowed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packageid', full_name='CTimedTrial_GetTimeRemaining_Response.packageid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mastersub_appid', full_name='CTimedTrial_GetTimeRemaining_Response.mastersub_appid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=150,
  serialized_end=282,
)


_CTIMEDTRIAL_RECORDPLAYTIME_REQUEST = _descriptor.Descriptor(
  name='CTimedTrial_RecordPlaytime_Request',
  full_name='CTimedTrial_RecordPlaytime_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CTimedTrial_RecordPlaytime_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds_played', full_name='CTimedTrial_RecordPlaytime_Request.seconds_played', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=284,
  serialized_end=359,
)


_CTIMEDTRIAL_RECORDPLAYTIME_RESPONSE = _descriptor.Descriptor(
  name='CTimedTrial_RecordPlaytime_Response',
  full_name='CTimedTrial_RecordPlaytime_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds_played', full_name='CTimedTrial_RecordPlaytime_Response.seconds_played', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds_allowed', full_name='CTimedTrial_RecordPlaytime_Response.seconds_allowed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=361,
  serialized_end=447,
)


_CTIMEDTRIAL_RESETPLAYTIME_REQUEST = _descriptor.Descriptor(
  name='CTimedTrial_ResetPlaytime_Request',
  full_name='CTimedTrial_ResetPlaytime_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CTimedTrial_ResetPlaytime_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=449,
  serialized_end=499,
)


_CTIMEDTRIAL_RESETPLAYTIME_RESPONSE = _descriptor.Descriptor(
  name='CTimedTrial_ResetPlaytime_Response',
  full_name='CTimedTrial_ResetPlaytime_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds_played', full_name='CTimedTrial_ResetPlaytime_Response.seconds_played', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds_allowed', full_name='CTimedTrial_ResetPlaytime_Response.seconds_allowed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=501,
  serialized_end=586,
)

DESCRIPTOR.message_types_by_name['CTimedTrial_GetTimeRemaining_Request'] = _CTIMEDTRIAL_GETTIMEREMAINING_REQUEST
DESCRIPTOR.message_types_by_name['CTimedTrial_GetTimeRemaining_Response'] = _CTIMEDTRIAL_GETTIMEREMAINING_RESPONSE
DESCRIPTOR.message_types_by_name['CTimedTrial_RecordPlaytime_Request'] = _CTIMEDTRIAL_RECORDPLAYTIME_REQUEST
DESCRIPTOR.message_types_by_name['CTimedTrial_RecordPlaytime_Response'] = _CTIMEDTRIAL_RECORDPLAYTIME_RESPONSE
DESCRIPTOR.message_types_by_name['CTimedTrial_ResetPlaytime_Request'] = _CTIMEDTRIAL_RESETPLAYTIME_REQUEST
DESCRIPTOR.message_types_by_name['CTimedTrial_ResetPlaytime_Response'] = _CTIMEDTRIAL_RESETPLAYTIME_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CTimedTrial_GetTimeRemaining_Request = _reflection.GeneratedProtocolMessageType('CTimedTrial_GetTimeRemaining_Request', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_GETTIMEREMAINING_REQUEST,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_GetTimeRemaining_Request)
  })
_sym_db.RegisterMessage(CTimedTrial_GetTimeRemaining_Request)

CTimedTrial_GetTimeRemaining_Response = _reflection.GeneratedProtocolMessageType('CTimedTrial_GetTimeRemaining_Response', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_GETTIMEREMAINING_RESPONSE,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_GetTimeRemaining_Response)
  })
_sym_db.RegisterMessage(CTimedTrial_GetTimeRemaining_Response)

CTimedTrial_RecordPlaytime_Request = _reflection.GeneratedProtocolMessageType('CTimedTrial_RecordPlaytime_Request', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_RECORDPLAYTIME_REQUEST,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_RecordPlaytime_Request)
  })
_sym_db.RegisterMessage(CTimedTrial_RecordPlaytime_Request)

CTimedTrial_RecordPlaytime_Response = _reflection.GeneratedProtocolMessageType('CTimedTrial_RecordPlaytime_Response', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_RECORDPLAYTIME_RESPONSE,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_RecordPlaytime_Response)
  })
_sym_db.RegisterMessage(CTimedTrial_RecordPlaytime_Response)

CTimedTrial_ResetPlaytime_Request = _reflection.GeneratedProtocolMessageType('CTimedTrial_ResetPlaytime_Request', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_RESETPLAYTIME_REQUEST,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_ResetPlaytime_Request)
  })
_sym_db.RegisterMessage(CTimedTrial_ResetPlaytime_Request)

CTimedTrial_ResetPlaytime_Response = _reflection.GeneratedProtocolMessageType('CTimedTrial_ResetPlaytime_Response', (_message.Message,), {
  'DESCRIPTOR' : _CTIMEDTRIAL_RESETPLAYTIME_RESPONSE,
  '__module__' : 'steammessages_timedtrial_pb2'
  # @@protoc_insertion_point(class_scope:CTimedTrial_ResetPlaytime_Response)
  })
_sym_db.RegisterMessage(CTimedTrial_ResetPlaytime_Response)


DESCRIPTOR._options = None

_TIMEDTRIAL = _descriptor.ServiceDescriptor(
  name='TimedTrial',
  full_name='TimedTrial',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\265\030-A service to get user timed trial information',
  create_key=_descriptor._internal_create_key,
  serialized_start=589,
  serialized_end=1128,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTimeRemaining',
    full_name='TimedTrial.GetTimeRemaining',
    index=0,
    containing_service=None,
    input_type=_CTIMEDTRIAL_GETTIMEREMAINING_REQUEST,
    output_type=_CTIMEDTRIAL_GETTIMEREMAINING_RESPONSE,
    serialized_options=b'\202\265\030FReturns the amount of time a user has left on a timed trial for an app',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RecordPlaytime',
    full_name='TimedTrial.RecordPlaytime',
    index=1,
    containing_service=None,
    input_type=_CTIMEDTRIAL_RECORDPLAYTIME_REQUEST,
    output_type=_CTIMEDTRIAL_RECORDPLAYTIME_RESPONSE,
    serialized_options=b'\202\265\0303Updates the user\'s remaining playtime while in game',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResetPlaytime',
    full_name='TimedTrial.ResetPlaytime',
    index=2,
    containing_service=None,
    input_type=_CTIMEDTRIAL_RESETPLAYTIME_REQUEST,
    output_type=_CTIMEDTRIAL_RESETPLAYTIME_RESPONSE,
    serialized_options=b'\202\265\0304Reset the user\'s remaining playtime (developer only)',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIMEDTRIAL)

DESCRIPTOR.services_by_name['TimedTrial'] = _TIMEDTRIAL

TimedTrial = service_reflection.GeneratedServiceType('TimedTrial', (_service.Service,), dict(
  DESCRIPTOR = _TIMEDTRIAL,
  __module__ = 'steammessages_timedtrial_pb2'
  ))

TimedTrial_Stub = service_reflection.GeneratedServiceStubType('TimedTrial_Stub', (TimedTrial,), dict(
  DESCRIPTOR = _TIMEDTRIAL,
  __module__ = 'steammessages_timedtrial_pb2'
  ))


# @@protoc_insertion_point(module_scope)
