# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waMmsRetry/WAMmsRetry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bwaMmsRetry/WAMmsRetry.proto\x12\nWAMmsRetry\"\xd0\x01\n\x16MediaRetryNotification\x12\x10\n\x08stanzaID\x18\x01 \x01(\t\x12\x12\n\ndirectPath\x18\x02 \x01(\t\x12=\n\x06result\x18\x03 \x01(\x0e\x32-.WAMmsRetry.MediaRetryNotification.ResultType\"Q\n\nResultType\x12\x11\n\rGENERAL_ERROR\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x12\x14\n\x10\x44\x45\x43RYPTION_ERROR\x10\x03\"&\n\x12ServerErrorReceipt\x12\x10\n\x08stanzaID\x18\x01 \x01(\tB&Z$go.mau.fi/whatsmeow/proto/waMmsRetry')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waMmsRetry.WAMmsRetry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$go.mau.fi/whatsmeow/proto/waMmsRetry'
  _MEDIARETRYNOTIFICATION._serialized_start=44
  _MEDIARETRYNOTIFICATION._serialized_end=252
  _MEDIARETRYNOTIFICATION_RESULTTYPE._serialized_start=171
  _MEDIARETRYNOTIFICATION_RESULTTYPE._serialized_end=252
  _SERVERERRORRECEIPT._serialized_start=254
  _SERVERERRORRECEIPT._serialized_end=292
# @@protoc_insertion_point(module_scope)
