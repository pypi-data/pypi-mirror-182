"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import arg_services.mining_explanation.v1.entailment_pb2
import grpc

class EntailmentExplanationServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Entailments: grpc.UnaryUnaryMultiCallable[
        arg_services.mining_explanation.v1.entailment_pb2.EntailmentsRequest,
        arg_services.mining_explanation.v1.entailment_pb2.EntailmentsResponse,
    ]

class EntailmentExplanationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Entailments(
        self,
        request: arg_services.mining_explanation.v1.entailment_pb2.EntailmentsRequest,
        context: grpc.ServicerContext,
    ) -> arg_services.mining_explanation.v1.entailment_pb2.EntailmentsResponse: ...

def add_EntailmentExplanationServiceServicer_to_server(servicer: EntailmentExplanationServiceServicer, server: grpc.Server) -> None: ...
