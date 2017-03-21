# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/rna_quantification_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import rna_quantification_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_rna__quantification__pb2
from ga4gh.schemas.google.api import annotations_pb2 as ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/rna_quantification_service.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n4ga4gh/schemas/ga4gh/rna_quantification_service.proto\x12\x13ga4gh.schemas.ga4gh\x1a,ga4gh/schemas/ga4gh/rna_quantification.proto\x1a*ga4gh/schemas/google/api/annotations.proto\"_\n\"SearchRnaQuantificationSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x8a\x01\n#SearchRnaQuantificationSetsResponse\x12J\n\x17rna_quantification_sets\x18\x01 \x03(\x0b\x32).ga4gh.schemas.ga4gh.RnaQuantificationSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"C\n\x1eGetRnaQuantificationSetRequest\x12!\n\x19rna_quantification_set_id\x18\x01 \x01(\t\"\x81\x01\n\x1fSearchRnaQuantificationsRequest\x12!\n\x19rna_quantification_set_id\x18\x01 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x80\x01\n SearchRnaQuantificationsResponse\x12\x43\n\x13rna_quantifications\x18\x01 \x03(\x0b\x32&.ga4gh.schemas.ga4gh.RnaQuantification\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"<\n\x1bGetRnaQuantificationRequest\x12\x1d\n\x15rna_quantification_id\x18\x01 \x01(\t\"\x87\x01\n\x1dSearchExpressionLevelsRequest\x12\x1d\n\x15rna_quantification_id\x18\x01 \x01(\t\x12\r\n\x05names\x18\x06 \x03(\t\x12\x11\n\tthreshold\x18\x03 \x01(\x02\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"z\n\x1eSearchExpressionLevelsResponse\x12?\n\x11\x65xpression_levels\x18\x01 \x03(\x0b\x32$.ga4gh.schemas.ga4gh.ExpressionLevel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"8\n\x19GetExpressionLevelRequest\x12\x1b\n\x13\x65xpression_level_id\x18\x01 \x01(\t2\xeb\x08\n\x18RnaQuantificationService\x12\xc4\x01\n\x1bSearchRnaQuantificationSets\x12\x37.ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest\x1a\x38.ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsResponse\"2\x82\xd3\xe4\x93\x02,\"\'/v0.6.0a10/rnaquantificationsets/search:\x01*\x12\xbf\x01\n\x17GetRnaQuantificationSet\x12\x33.ga4gh.schemas.ga4gh.GetRnaQuantificationSetRequest\x1a).ga4gh.schemas.ga4gh.RnaQuantificationSet\"D\x82\xd3\xe4\x93\x02>\x12</v0.6.0a10/rnaquantificationsets/{rna_quantification_set_id}\x12\xb8\x01\n\x18SearchRnaQuantifications\x12\x34.ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest\x1a\x35.ga4gh.schemas.ga4gh.SearchRnaQuantificationsResponse\"/\x82\xd3\xe4\x93\x02)\"$/v0.6.0a10/rnaquantifications/search:\x01*\x12\xaf\x01\n\x14GetRnaQuantification\x12\x30.ga4gh.schemas.ga4gh.GetRnaQuantificationRequest\x1a&.ga4gh.schemas.ga4gh.RnaQuantification\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v0.6.0a10/rnaquantifications/{rna_quantification_id}\x12\xb0\x01\n\x16SearchExpressionLevels\x12\x32.ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest\x1a\x33.ga4gh.schemas.ga4gh.SearchExpressionLevelsResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/v0.6.0a10/expressionlevels/search:\x01*\x12\xa5\x01\n\x12GetExpressionLevel\x12..ga4gh.schemas.ga4gh.GetExpressionLevelRequest\x1a$.ga4gh.schemas.ga4gh.ExpressionLevel\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v0.6.0a10/expressionlevels/{expression_level_id}b\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_rna__quantification__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHRNAQUANTIFICATIONSETSREQUEST = _descriptor.Descriptor(
  name='SearchRnaQuantificationSetsRequest',
  full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=262,
)


_SEARCHRNAQUANTIFICATIONSETSRESPONSE = _descriptor.Descriptor(
  name='SearchRnaQuantificationSetsResponse',
  full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantification_sets', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsResponse.rna_quantification_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=403,
)


_GETRNAQUANTIFICATIONSETREQUEST = _descriptor.Descriptor(
  name='GetRnaQuantificationSetRequest',
  full_name='ga4gh.schemas.ga4gh.GetRnaQuantificationSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantification_set_id', full_name='ga4gh.schemas.ga4gh.GetRnaQuantificationSetRequest.rna_quantification_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=472,
)


_SEARCHRNAQUANTIFICATIONSREQUEST = _descriptor.Descriptor(
  name='SearchRnaQuantificationsRequest',
  full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantification_set_id', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest.rna_quantification_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest.biosample_id', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest.page_size', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest.page_token', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=604,
)


_SEARCHRNAQUANTIFICATIONSRESPONSE = _descriptor.Descriptor(
  name='SearchRnaQuantificationsResponse',
  full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantifications', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsResponse.rna_quantifications', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchRnaQuantificationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=735,
)


_GETRNAQUANTIFICATIONREQUEST = _descriptor.Descriptor(
  name='GetRnaQuantificationRequest',
  full_name='ga4gh.schemas.ga4gh.GetRnaQuantificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantification_id', full_name='ga4gh.schemas.ga4gh.GetRnaQuantificationRequest.rna_quantification_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=797,
)


_SEARCHEXPRESSIONLEVELSREQUEST = _descriptor.Descriptor(
  name='SearchExpressionLevelsRequest',
  full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rna_quantification_id', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest.rna_quantification_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest.names', index=1,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest.threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=935,
)


_SEARCHEXPRESSIONLEVELSRESPONSE = _descriptor.Descriptor(
  name='SearchExpressionLevelsResponse',
  full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='expression_levels', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsResponse.expression_levels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchExpressionLevelsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=937,
  serialized_end=1059,
)


_GETEXPRESSIONLEVELREQUEST = _descriptor.Descriptor(
  name='GetExpressionLevelRequest',
  full_name='ga4gh.schemas.ga4gh.GetExpressionLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='expression_level_id', full_name='ga4gh.schemas.ga4gh.GetExpressionLevelRequest.expression_level_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1061,
  serialized_end=1117,
)

_SEARCHRNAQUANTIFICATIONSETSRESPONSE.fields_by_name['rna_quantification_sets'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_rna__quantification__pb2._RNAQUANTIFICATIONSET
_SEARCHRNAQUANTIFICATIONSRESPONSE.fields_by_name['rna_quantifications'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_rna__quantification__pb2._RNAQUANTIFICATION
_SEARCHEXPRESSIONLEVELSRESPONSE.fields_by_name['expression_levels'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_rna__quantification__pb2._EXPRESSIONLEVEL
DESCRIPTOR.message_types_by_name['SearchRnaQuantificationSetsRequest'] = _SEARCHRNAQUANTIFICATIONSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchRnaQuantificationSetsResponse'] = _SEARCHRNAQUANTIFICATIONSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetRnaQuantificationSetRequest'] = _GETRNAQUANTIFICATIONSETREQUEST
DESCRIPTOR.message_types_by_name['SearchRnaQuantificationsRequest'] = _SEARCHRNAQUANTIFICATIONSREQUEST
DESCRIPTOR.message_types_by_name['SearchRnaQuantificationsResponse'] = _SEARCHRNAQUANTIFICATIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetRnaQuantificationRequest'] = _GETRNAQUANTIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['SearchExpressionLevelsRequest'] = _SEARCHEXPRESSIONLEVELSREQUEST
DESCRIPTOR.message_types_by_name['SearchExpressionLevelsResponse'] = _SEARCHEXPRESSIONLEVELSRESPONSE
DESCRIPTOR.message_types_by_name['GetExpressionLevelRequest'] = _GETEXPRESSIONLEVELREQUEST

SearchRnaQuantificationSetsRequest = _reflection.GeneratedProtocolMessageType('SearchRnaQuantificationSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRNAQUANTIFICATIONSETSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsRequest)
  ))
_sym_db.RegisterMessage(SearchRnaQuantificationSetsRequest)

SearchRnaQuantificationSetsResponse = _reflection.GeneratedProtocolMessageType('SearchRnaQuantificationSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRNAQUANTIFICATIONSETSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchRnaQuantificationSetsResponse)
  ))
_sym_db.RegisterMessage(SearchRnaQuantificationSetsResponse)

GetRnaQuantificationSetRequest = _reflection.GeneratedProtocolMessageType('GetRnaQuantificationSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRNAQUANTIFICATIONSETREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetRnaQuantificationSetRequest)
  ))
_sym_db.RegisterMessage(GetRnaQuantificationSetRequest)

SearchRnaQuantificationsRequest = _reflection.GeneratedProtocolMessageType('SearchRnaQuantificationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRNAQUANTIFICATIONSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchRnaQuantificationsRequest)
  ))
_sym_db.RegisterMessage(SearchRnaQuantificationsRequest)

SearchRnaQuantificationsResponse = _reflection.GeneratedProtocolMessageType('SearchRnaQuantificationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRNAQUANTIFICATIONSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchRnaQuantificationsResponse)
  ))
_sym_db.RegisterMessage(SearchRnaQuantificationsResponse)

GetRnaQuantificationRequest = _reflection.GeneratedProtocolMessageType('GetRnaQuantificationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRNAQUANTIFICATIONREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetRnaQuantificationRequest)
  ))
_sym_db.RegisterMessage(GetRnaQuantificationRequest)

SearchExpressionLevelsRequest = _reflection.GeneratedProtocolMessageType('SearchExpressionLevelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPRESSIONLEVELSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchExpressionLevelsRequest)
  ))
_sym_db.RegisterMessage(SearchExpressionLevelsRequest)

SearchExpressionLevelsResponse = _reflection.GeneratedProtocolMessageType('SearchExpressionLevelsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPRESSIONLEVELSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchExpressionLevelsResponse)
  ))
_sym_db.RegisterMessage(SearchExpressionLevelsResponse)

GetExpressionLevelRequest = _reflection.GeneratedProtocolMessageType('GetExpressionLevelRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPRESSIONLEVELREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.rna_quantification_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetExpressionLevelRequest)
  ))
_sym_db.RegisterMessage(GetExpressionLevelRequest)


# @@protoc_insertion_point(module_scope)
