"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import arg_services.graph.v1.graph_pb2
import arg_services.nlp.v1.nlp_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MappingAlgorithm:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MappingAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MappingAlgorithm.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MAPPING_ALGORITHM_UNSPECIFIED: _MappingAlgorithm.ValueType  # 0
    MAPPING_ALGORITHM_ASTAR: _MappingAlgorithm.ValueType  # 1
    MAPPING_ALGORITHM_ISOMORPHISM: _MappingAlgorithm.ValueType  # 2

class MappingAlgorithm(_MappingAlgorithm, metaclass=_MappingAlgorithmEnumTypeWrapper): ...

MAPPING_ALGORITHM_UNSPECIFIED: MappingAlgorithm.ValueType  # 0
MAPPING_ALGORITHM_ASTAR: MappingAlgorithm.ValueType  # 1
MAPPING_ALGORITHM_ISOMORPHISM: MappingAlgorithm.ValueType  # 2
global___MappingAlgorithm = MappingAlgorithm

@typing_extensions.final
class RetrieveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class CasesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> arg_services.graph.v1.graph_pb2.Graph: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: arg_services.graph.v1.graph_pb2.Graph | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    CASES_FIELD_NUMBER: builtins.int
    QUERY_GRAPH_FIELD_NUMBER: builtins.int
    QUERY_TEXT_FIELD_NUMBER: builtins.int
    NLP_CONFIG_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    MAC_PHASE_FIELD_NUMBER: builtins.int
    FAC_PHASE_FIELD_NUMBER: builtins.int
    MAPPING_ALGORITHM_FIELD_NUMBER: builtins.int
    USE_SCHEME_ONTOLOGY_FIELD_NUMBER: builtins.int
    ENFORCE_SCHEME_TYPES_FIELD_NUMBER: builtins.int
    EXTRAS_FIELD_NUMBER: builtins.int
    @property
    def cases(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, arg_services.graph.v1.graph_pb2.Graph]: ...
    @property
    def query_graph(self) -> arg_services.graph.v1.graph_pb2.Graph: ...
    query_text: builtins.str
    @property
    def nlp_config(self) -> arg_services.nlp.v1.nlp_pb2.NlpConfig: ...
    limit: builtins.int
    mac_phase: builtins.bool
    fac_phase: builtins.bool
    mapping_algorithm: global___MappingAlgorithm.ValueType
    use_scheme_ontology: builtins.bool
    enforce_scheme_types: builtins.bool
    @property
    def extras(self) -> google.protobuf.struct_pb2.Struct:
        """Implementation-specific information can be encoded here"""
    def __init__(
        self,
        *,
        cases: collections.abc.Mapping[builtins.str, arg_services.graph.v1.graph_pb2.Graph] | None = ...,
        query_graph: arg_services.graph.v1.graph_pb2.Graph | None = ...,
        query_text: builtins.str = ...,
        nlp_config: arg_services.nlp.v1.nlp_pb2.NlpConfig | None = ...,
        limit: builtins.int = ...,
        mac_phase: builtins.bool = ...,
        fac_phase: builtins.bool = ...,
        mapping_algorithm: global___MappingAlgorithm.ValueType = ...,
        use_scheme_ontology: builtins.bool = ...,
        enforce_scheme_types: builtins.bool = ...,
        extras: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extras", b"extras", "nlp_config", b"nlp_config", "query", b"query", "query_graph", b"query_graph", "query_text", b"query_text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cases", b"cases", "enforce_scheme_types", b"enforce_scheme_types", "extras", b"extras", "fac_phase", b"fac_phase", "limit", b"limit", "mac_phase", b"mac_phase", "mapping_algorithm", b"mapping_algorithm", "nlp_config", b"nlp_config", "query", b"query", "query_graph", b"query_graph", "query_text", b"query_text", "use_scheme_ontology", b"use_scheme_ontology"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["query", b"query"]) -> typing_extensions.Literal["query_graph", "query_text"] | None: ...

global___RetrieveRequest = RetrieveRequest

@typing_extensions.final
class RetrieveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RANKING_FIELD_NUMBER: builtins.int
    MAC_RANKING_FIELD_NUMBER: builtins.int
    FAC_RANKING_FIELD_NUMBER: builtins.int
    EXTRAS_FIELD_NUMBER: builtins.int
    @property
    def ranking(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RetrievedCase]: ...
    @property
    def mac_ranking(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RetrievedCase]: ...
    @property
    def fac_ranking(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RetrievedMapping]: ...
    @property
    def extras(self) -> google.protobuf.struct_pb2.Struct:
        """Implementation-specific information can be encoded here"""
    def __init__(
        self,
        *,
        ranking: collections.abc.Iterable[global___RetrievedCase] | None = ...,
        mac_ranking: collections.abc.Iterable[global___RetrievedCase] | None = ...,
        fac_ranking: collections.abc.Iterable[global___RetrievedMapping] | None = ...,
        extras: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extras", b"extras"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["extras", b"extras", "fac_ranking", b"fac_ranking", "mac_ranking", b"mac_ranking", "ranking", b"ranking"]) -> None: ...

global___RetrieveResponse = RetrieveResponse

@typing_extensions.final
class RetrievedCase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    id: builtins.str
    similarity: builtins.float
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        similarity: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "similarity", b"similarity"]) -> None: ...

global___RetrievedCase = RetrievedCase

@typing_extensions.final
class RetrievedMapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CASE_FIELD_NUMBER: builtins.int
    NODE_MAPPINGS_FIELD_NUMBER: builtins.int
    @property
    def case(self) -> global___RetrievedCase: ...
    @property
    def node_mappings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Mapping]: ...
    def __init__(
        self,
        *,
        case: global___RetrievedCase | None = ...,
        node_mappings: collections.abc.Iterable[global___Mapping] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["case", b"case"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["case", b"case", "node_mappings", b"node_mappings"]) -> None: ...

global___RetrievedMapping = RetrievedMapping

@typing_extensions.final
class Mapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_ID_FIELD_NUMBER: builtins.int
    CASE_ID_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    query_id: builtins.str
    case_id: builtins.str
    similarity: builtins.float
    def __init__(
        self,
        *,
        query_id: builtins.str = ...,
        case_id: builtins.str = ...,
        similarity: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["case_id", b"case_id", "query_id", b"query_id", "similarity", b"similarity"]) -> None: ...

global___Mapping = Mapping
