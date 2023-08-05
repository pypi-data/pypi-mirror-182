# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iamanager/v2/iamanagerprotected.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from aos_prov.communication.unit.v2.generated import iamanagercommon_pb2 as iamanager_dot_v2_dot_iamanagercommon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='iamanager/v2/iamanagerprotected.proto',
  package='iamanager.v2',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%iamanager/v2/iamanagerprotected.proto\x12\x0ciamanager.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\"iamanager/v2/iamanagercommon.proto\"\x1c\n\x0c\x43learRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"1\n\x0fSetOwnerRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"2\n\x10\x43reateKeyRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\".\n\x11\x43reateKeyResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03\x63sr\x18\x02 \x01(\t\".\n\x10\x41pplyCertRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x63\x65rt\x18\x02 \x01(\t\"3\n\x11\x41pplyCertResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08\x63\x65rt_url\x18\x02 \x01(\t\"\xc7\x01\n\x16RegisterServiceRequest\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12J\n\x0bpermissions\x18\x02 \x03(\x0b\x32\x35.iamanager.v2.RegisterServiceRequest.PermissionsEntry\x1aM\n\x10PermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.iamanager.v2.Permissions:\x02\x38\x01\")\n\x17RegisterServiceResponse\x12\x0e\n\x06secret\x18\x01 \x01(\t\".\n\x18UnregisterServiceRequest\x12\x12\n\nservice_id\x18\x01 \x01(\t\"&\n\x12\x45ncryptDiskRequest\x12\x10\n\x08password\x18\x01 \x01(\t2\xc0\x05\n\x13IAMProtectedService\x12\x43\n\x08SetOwner\x12\x1d.iamanager.v2.SetOwnerRequest\x1a\x16.google.protobuf.Empty\"\x00\x12=\n\x05\x43lear\x12\x1a.iamanager.v2.ClearRequest\x1a\x16.google.protobuf.Empty\"\x00\x12N\n\tCreateKey\x12\x1e.iamanager.v2.CreateKeyRequest\x1a\x1f.iamanager.v2.CreateKeyResponse\"\x00\x12N\n\tApplyCert\x12\x1e.iamanager.v2.ApplyCertRequest\x1a\x1f.iamanager.v2.ApplyCertResponse\"\x00\x12I\n\x0b\x45ncryptDisk\x12 .iamanager.v2.EncryptDiskRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\x12\x46inishProvisioning\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x39\n\x08SetUsers\x12\x13.iamanager.v2.Users\x1a\x16.google.protobuf.Empty\"\x00\x12`\n\x0fRegisterService\x12$.iamanager.v2.RegisterServiceRequest\x1a%.iamanager.v2.RegisterServiceResponse\"\x00\x12U\n\x11UnregisterService\x12&.iamanager.v2.UnregisterServiceRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,iamanager_dot_v2_dot_iamanagercommon__pb2.DESCRIPTOR,])




_CLEARREQUEST = _descriptor.Descriptor(
  name='ClearRequest',
  full_name='iamanager.v2.ClearRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.ClearRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=120,
  serialized_end=148,
)


_SETOWNERREQUEST = _descriptor.Descriptor(
  name='SetOwnerRequest',
  full_name='iamanager.v2.SetOwnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.SetOwnerRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='iamanager.v2.SetOwnerRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=150,
  serialized_end=199,
)


_CREATEKEYREQUEST = _descriptor.Descriptor(
  name='CreateKeyRequest',
  full_name='iamanager.v2.CreateKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.CreateKeyRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='iamanager.v2.CreateKeyRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=201,
  serialized_end=251,
)


_CREATEKEYRESPONSE = _descriptor.Descriptor(
  name='CreateKeyResponse',
  full_name='iamanager.v2.CreateKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.CreateKeyResponse.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='csr', full_name='iamanager.v2.CreateKeyResponse.csr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=253,
  serialized_end=299,
)


_APPLYCERTREQUEST = _descriptor.Descriptor(
  name='ApplyCertRequest',
  full_name='iamanager.v2.ApplyCertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.ApplyCertRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cert', full_name='iamanager.v2.ApplyCertRequest.cert', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=301,
  serialized_end=347,
)


_APPLYCERTRESPONSE = _descriptor.Descriptor(
  name='ApplyCertResponse',
  full_name='iamanager.v2.ApplyCertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iamanager.v2.ApplyCertResponse.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cert_url', full_name='iamanager.v2.ApplyCertResponse.cert_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=349,
  serialized_end=400,
)


_REGISTERSERVICEREQUEST_PERMISSIONSENTRY = _descriptor.Descriptor(
  name='PermissionsEntry',
  full_name='iamanager.v2.RegisterServiceRequest.PermissionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='iamanager.v2.RegisterServiceRequest.PermissionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='iamanager.v2.RegisterServiceRequest.PermissionsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=602,
)

_REGISTERSERVICEREQUEST = _descriptor.Descriptor(
  name='RegisterServiceRequest',
  full_name='iamanager.v2.RegisterServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_id', full_name='iamanager.v2.RegisterServiceRequest.service_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='iamanager.v2.RegisterServiceRequest.permissions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REGISTERSERVICEREQUEST_PERMISSIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=602,
)


_REGISTERSERVICERESPONSE = _descriptor.Descriptor(
  name='RegisterServiceResponse',
  full_name='iamanager.v2.RegisterServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='iamanager.v2.RegisterServiceResponse.secret', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=604,
  serialized_end=645,
)


_UNREGISTERSERVICEREQUEST = _descriptor.Descriptor(
  name='UnregisterServiceRequest',
  full_name='iamanager.v2.UnregisterServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_id', full_name='iamanager.v2.UnregisterServiceRequest.service_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=647,
  serialized_end=693,
)


_ENCRYPTDISKREQUEST = _descriptor.Descriptor(
  name='EncryptDiskRequest',
  full_name='iamanager.v2.EncryptDiskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='iamanager.v2.EncryptDiskRequest.password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=695,
  serialized_end=733,
)

_REGISTERSERVICEREQUEST_PERMISSIONSENTRY.fields_by_name['value'].message_type = iamanager_dot_v2_dot_iamanagercommon__pb2._PERMISSIONS
_REGISTERSERVICEREQUEST_PERMISSIONSENTRY.containing_type = _REGISTERSERVICEREQUEST
_REGISTERSERVICEREQUEST.fields_by_name['permissions'].message_type = _REGISTERSERVICEREQUEST_PERMISSIONSENTRY
DESCRIPTOR.message_types_by_name['ClearRequest'] = _CLEARREQUEST
DESCRIPTOR.message_types_by_name['SetOwnerRequest'] = _SETOWNERREQUEST
DESCRIPTOR.message_types_by_name['CreateKeyRequest'] = _CREATEKEYREQUEST
DESCRIPTOR.message_types_by_name['CreateKeyResponse'] = _CREATEKEYRESPONSE
DESCRIPTOR.message_types_by_name['ApplyCertRequest'] = _APPLYCERTREQUEST
DESCRIPTOR.message_types_by_name['ApplyCertResponse'] = _APPLYCERTRESPONSE
DESCRIPTOR.message_types_by_name['RegisterServiceRequest'] = _REGISTERSERVICEREQUEST
DESCRIPTOR.message_types_by_name['RegisterServiceResponse'] = _REGISTERSERVICERESPONSE
DESCRIPTOR.message_types_by_name['UnregisterServiceRequest'] = _UNREGISTERSERVICEREQUEST
DESCRIPTOR.message_types_by_name['EncryptDiskRequest'] = _ENCRYPTDISKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClearRequest = _reflection.GeneratedProtocolMessageType('ClearRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEARREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.ClearRequest)
  })
_sym_db.RegisterMessage(ClearRequest)

SetOwnerRequest = _reflection.GeneratedProtocolMessageType('SetOwnerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETOWNERREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.SetOwnerRequest)
  })
_sym_db.RegisterMessage(SetOwnerRequest)

CreateKeyRequest = _reflection.GeneratedProtocolMessageType('CreateKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEKEYREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.CreateKeyRequest)
  })
_sym_db.RegisterMessage(CreateKeyRequest)

CreateKeyResponse = _reflection.GeneratedProtocolMessageType('CreateKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEKEYRESPONSE,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.CreateKeyResponse)
  })
_sym_db.RegisterMessage(CreateKeyResponse)

ApplyCertRequest = _reflection.GeneratedProtocolMessageType('ApplyCertRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPLYCERTREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.ApplyCertRequest)
  })
_sym_db.RegisterMessage(ApplyCertRequest)

ApplyCertResponse = _reflection.GeneratedProtocolMessageType('ApplyCertResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYCERTRESPONSE,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.ApplyCertResponse)
  })
_sym_db.RegisterMessage(ApplyCertResponse)

RegisterServiceRequest = _reflection.GeneratedProtocolMessageType('RegisterServiceRequest', (_message.Message,), {

  'PermissionsEntry' : _reflection.GeneratedProtocolMessageType('PermissionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERSERVICEREQUEST_PERMISSIONSENTRY,
    '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
    # @@protoc_insertion_point(class_scope:iamanager.v2.RegisterServiceRequest.PermissionsEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERSERVICEREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.RegisterServiceRequest)
  })
_sym_db.RegisterMessage(RegisterServiceRequest)
_sym_db.RegisterMessage(RegisterServiceRequest.PermissionsEntry)

RegisterServiceResponse = _reflection.GeneratedProtocolMessageType('RegisterServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERSERVICERESPONSE,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.RegisterServiceResponse)
  })
_sym_db.RegisterMessage(RegisterServiceResponse)

UnregisterServiceRequest = _reflection.GeneratedProtocolMessageType('UnregisterServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNREGISTERSERVICEREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.UnregisterServiceRequest)
  })
_sym_db.RegisterMessage(UnregisterServiceRequest)

EncryptDiskRequest = _reflection.GeneratedProtocolMessageType('EncryptDiskRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTDISKREQUEST,
  '__module__' : 'iamanager.v2.iamanagerprotected_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.v2.EncryptDiskRequest)
  })
_sym_db.RegisterMessage(EncryptDiskRequest)


_REGISTERSERVICEREQUEST_PERMISSIONSENTRY._options = None

_IAMPROTECTEDSERVICE = _descriptor.ServiceDescriptor(
  name='IAMProtectedService',
  full_name='iamanager.v2.IAMProtectedService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=736,
  serialized_end=1440,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetOwner',
    full_name='iamanager.v2.IAMProtectedService.SetOwner',
    index=0,
    containing_service=None,
    input_type=_SETOWNERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Clear',
    full_name='iamanager.v2.IAMProtectedService.Clear',
    index=1,
    containing_service=None,
    input_type=_CLEARREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateKey',
    full_name='iamanager.v2.IAMProtectedService.CreateKey',
    index=2,
    containing_service=None,
    input_type=_CREATEKEYREQUEST,
    output_type=_CREATEKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyCert',
    full_name='iamanager.v2.IAMProtectedService.ApplyCert',
    index=3,
    containing_service=None,
    input_type=_APPLYCERTREQUEST,
    output_type=_APPLYCERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EncryptDisk',
    full_name='iamanager.v2.IAMProtectedService.EncryptDisk',
    index=4,
    containing_service=None,
    input_type=_ENCRYPTDISKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FinishProvisioning',
    full_name='iamanager.v2.IAMProtectedService.FinishProvisioning',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetUsers',
    full_name='iamanager.v2.IAMProtectedService.SetUsers',
    index=6,
    containing_service=None,
    input_type=iamanager_dot_v2_dot_iamanagercommon__pb2._USERS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterService',
    full_name='iamanager.v2.IAMProtectedService.RegisterService',
    index=7,
    containing_service=None,
    input_type=_REGISTERSERVICEREQUEST,
    output_type=_REGISTERSERVICERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterService',
    full_name='iamanager.v2.IAMProtectedService.UnregisterService',
    index=8,
    containing_service=None,
    input_type=_UNREGISTERSERVICEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IAMPROTECTEDSERVICE)

DESCRIPTOR.services_by_name['IAMProtectedService'] = _IAMPROTECTEDSERVICE

# @@protoc_insertion_point(module_scope)
