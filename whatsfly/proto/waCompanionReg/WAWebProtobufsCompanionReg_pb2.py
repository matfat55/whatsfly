# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waCompanionReg/WAWebProtobufsCompanionReg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/waCompanionReg/WAWebProtobufsCompanionReg.proto\x12\x1aWAWebProtobufsCompanionReg\"\xf9\x08\n\x0b\x44\x65viceProps\x12\n\n\x02os\x18\x01 \x01(\t\x12\x43\n\x07version\x18\x02 \x01(\x0b\x32\x32.WAWebProtobufsCompanionReg.DeviceProps.AppVersion\x12J\n\x0cplatformType\x18\x03 \x01(\x0e\x32\x34.WAWebProtobufsCompanionReg.DeviceProps.PlatformType\x12\x17\n\x0frequireFullSync\x18\x04 \x01(\x08\x12T\n\x11historySyncConfig\x18\x05 \x01(\x0b\x32\x39.WAWebProtobufsCompanionReg.DeviceProps.HistorySyncConfig\x1a\xa4\x03\n\x11HistorySyncConfig\x12\x19\n\x11\x66ullSyncDaysLimit\x18\x01 \x01(\r\x12\x1b\n\x13\x66ullSyncSizeMbLimit\x18\x02 \x01(\r\x12\x16\n\x0estorageQuotaMb\x18\x03 \x01(\r\x12%\n\x1dinlineInitialPayloadInE2EeMsg\x18\x04 \x01(\x08\x12\x1b\n\x13recentSyncDaysLimit\x18\x05 \x01(\r\x12\x1d\n\x15supportCallLogHistory\x18\x06 \x01(\x08\x12&\n\x1esupportBotUserAgentChatHistory\x18\x07 \x01(\x08\x12#\n\x1bsupportCagReactionsAndPolls\x18\x08 \x01(\x08\x12\x1b\n\x13supportBizHostedMsg\x18\t \x01(\x08\x12\x30\n(supportRecentSyncChunkMessageCountTuning\x18\n \x01(\x08\x12\x1d\n\x15supportHostedGroupMsg\x18\x0b \x01(\x08\x12!\n\x19supportFbidBotChatHistory\x18\x0c \x01(\x08\x1ag\n\nAppVersion\x12\x0f\n\x07primary\x18\x01 \x01(\r\x12\x11\n\tsecondary\x18\x02 \x01(\r\x12\x10\n\x08tertiary\x18\x03 \x01(\r\x12\x12\n\nquaternary\x18\x04 \x01(\r\x12\x0f\n\x07quinary\x18\x05 \x01(\r\"\xcd\x02\n\x0cPlatformType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43HROME\x10\x01\x12\x0b\n\x07\x46IREFOX\x10\x02\x12\x06\n\x02IE\x10\x03\x12\t\n\x05OPERA\x10\x04\x12\n\n\x06SAFARI\x10\x05\x12\x08\n\x04\x45\x44GE\x10\x06\x12\x0b\n\x07\x44\x45SKTOP\x10\x07\x12\x08\n\x04IPAD\x10\x08\x12\x12\n\x0e\x41NDROID_TABLET\x10\t\x12\t\n\x05OHANA\x10\n\x12\t\n\x05\x41LOHA\x10\x0b\x12\x0c\n\x08\x43\x41TALINA\x10\x0c\x12\n\n\x06TCL_TV\x10\r\x12\r\n\tIOS_PHONE\x10\x0e\x12\x10\n\x0cIOS_CATALYST\x10\x0f\x12\x11\n\rANDROID_PHONE\x10\x10\x12\x15\n\x11\x41NDROID_AMBIGUOUS\x10\x11\x12\x0b\n\x07WEAR_OS\x10\x12\x12\x0c\n\x08\x41R_WRIST\x10\x13\x12\r\n\tAR_DEVICE\x10\x14\x12\x07\n\x03UWP\x10\x15\x12\x06\n\x02VR\x10\x16\x12\r\n\tCLOUD_API\x10\x17\"\x86\x01\n\x1a\x43ompanionEphemeralIdentity\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\x12H\n\ndeviceType\x18\x02 \x01(\x0e\x32\x34.WAWebProtobufsCompanionReg.DeviceProps.PlatformType\x12\x0b\n\x03ref\x18\x03 \x01(\t\"-\n\x18PrimaryEphemeralIdentity\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\"?\n\x17\x45ncryptedPairingRequest\x12\x18\n\x10\x65ncryptedPayload\x18\x01 \x01(\x0c\x12\n\n\x02IV\x18\x02 \x01(\x0c\"1\n\x12\x43lientPairingProps\x12\x1b\n\x13isChatDbLidMigrated\x18\x01 \x01(\x08\x42*Z(go.mau.fi/whatsmeow/proto/waCompanionReg')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waCompanionReg.WAWebProtobufsCompanionReg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(go.mau.fi/whatsmeow/proto/waCompanionReg'
  _DEVICEPROPS._serialized_start=80
  _DEVICEPROPS._serialized_end=1225
  _DEVICEPROPS_HISTORYSYNCCONFIG._serialized_start=364
  _DEVICEPROPS_HISTORYSYNCCONFIG._serialized_end=784
  _DEVICEPROPS_APPVERSION._serialized_start=786
  _DEVICEPROPS_APPVERSION._serialized_end=889
  _DEVICEPROPS_PLATFORMTYPE._serialized_start=892
  _DEVICEPROPS_PLATFORMTYPE._serialized_end=1225
  _COMPANIONEPHEMERALIDENTITY._serialized_start=1228
  _COMPANIONEPHEMERALIDENTITY._serialized_end=1362
  _PRIMARYEPHEMERALIDENTITY._serialized_start=1364
  _PRIMARYEPHEMERALIDENTITY._serialized_end=1409
  _ENCRYPTEDPAIRINGREQUEST._serialized_start=1411
  _ENCRYPTEDPAIRINGREQUEST._serialized_end=1474
  _CLIENTPAIRINGPROPS._serialized_start=1476
  _CLIENTPAIRINGPROPS._serialized_end=1525
# @@protoc_insertion_point(module_scope)
