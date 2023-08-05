"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import arg_services.mining_explanation.v1.adu_pb2
import grpc

class AduExplanationServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Classification: grpc.UnaryUnaryMultiCallable[
        arg_services.mining_explanation.v1.adu_pb2.ClassificationRequest,
        arg_services.mining_explanation.v1.adu_pb2.ClassificationResponse,
    ]

class AduExplanationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Classification(
        self,
        request: arg_services.mining_explanation.v1.adu_pb2.ClassificationRequest,
        context: grpc.ServicerContext,
    ) -> arg_services.mining_explanation.v1.adu_pb2.ClassificationResponse: ...

def add_AduExplanationServiceServicer_to_server(servicer: AduExplanationServiceServicer, server: grpc.Server) -> None: ...
