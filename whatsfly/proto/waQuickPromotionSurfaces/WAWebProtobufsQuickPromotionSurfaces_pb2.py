# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waQuickPromotionSurfaces/WAWebProtobufsQuickPromotionSurfaces.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCwaQuickPromotionSurfaces/WAWebProtobufsQuickPromotionSurfaces.proto\x12$WAWebProtobufsQuickPromotionSurfaces\"\xe4\x05\n\x02QP\x1a\xe1\x01\n\x0c\x46ilterClause\x12G\n\nclauseType\x18\x01 \x02(\x0e\x32\x33.WAWebProtobufsQuickPromotionSurfaces.QP.ClauseType\x12\x46\n\x07\x63lauses\x18\x02 \x03(\x0b\x32\x35.WAWebProtobufsQuickPromotionSurfaces.QP.FilterClause\x12@\n\x07\x66ilters\x18\x03 \x03(\x0b\x32/.WAWebProtobufsQuickPromotionSurfaces.QP.Filter\x1a\xa3\x02\n\x06\x46ilter\x12\x12\n\nfilterName\x18\x01 \x02(\t\x12M\n\nparameters\x18\x02 \x03(\x0b\x32\x39.WAWebProtobufsQuickPromotionSurfaces.QP.FilterParameters\x12K\n\x0c\x66ilterResult\x18\x03 \x01(\x0e\x32\x35.WAWebProtobufsQuickPromotionSurfaces.QP.FilterResult\x12i\n\x18\x63lientNotSupportedConfig\x18\x04 \x02(\x0e\x32G.WAWebProtobufsQuickPromotionSurfaces.QP.FilterClientNotSupportedConfig\x1a.\n\x10\x46ilterParameters\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"0\n\x0c\x46ilterResult\x12\x08\n\x04TRUE\x10\x01\x12\t\n\x05\x46\x41LSE\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\"J\n\x1e\x46ilterClientNotSupportedConfig\x12\x13\n\x0fPASS_BY_DEFAULT\x10\x01\x12\x13\n\x0f\x46\x41IL_BY_DEFAULT\x10\x02\"&\n\nClauseType\x12\x07\n\x03\x41ND\x10\x01\x12\x06\n\x02OR\x10\x02\x12\x07\n\x03NOR\x10\x03\x42\x34Z2go.mau.fi/whatsmeow/proto/waQuickPromotionSurfaces')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waQuickPromotionSurfaces.WAWebProtobufsQuickPromotionSurfaces_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2go.mau.fi/whatsmeow/proto/waQuickPromotionSurfaces'
  _QP._serialized_start=110
  _QP._serialized_end=850
  _QP_FILTERCLAUSE._serialized_start=117
  _QP_FILTERCLAUSE._serialized_end=342
  _QP_FILTER._serialized_start=345
  _QP_FILTER._serialized_end=636
  _QP_FILTERPARAMETERS._serialized_start=638
  _QP_FILTERPARAMETERS._serialized_end=684
  _QP_FILTERRESULT._serialized_start=686
  _QP_FILTERRESULT._serialized_end=734
  _QP_FILTERCLIENTNOTSUPPORTEDCONFIG._serialized_start=736
  _QP_FILTERCLIENTNOTSUPPORTEDCONFIG._serialized_end=810
  _QP_CLAUSETYPE._serialized_start=812
  _QP_CLAUSETYPE._serialized_end=850
# @@protoc_insertion_point(module_scope)
