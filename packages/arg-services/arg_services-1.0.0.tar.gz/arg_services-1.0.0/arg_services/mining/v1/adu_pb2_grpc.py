# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from arg_services.mining.v1 import adu_pb2 as arg__services_dot_mining_dot_v1_dot_adu__pb2


class AduServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Segmentation = channel.unary_unary(
                '/arg_services.mining.v1.AduService/Segmentation',
                request_serializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationRequest.SerializeToString,
                response_deserializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationResponse.FromString,
                )
        self.Classification = channel.unary_unary(
                '/arg_services.mining.v1.AduService/Classification',
                request_serializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationRequest.SerializeToString,
                response_deserializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationResponse.FromString,
                )


class AduServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Segmentation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Classification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AduServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Segmentation': grpc.unary_unary_rpc_method_handler(
                    servicer.Segmentation,
                    request_deserializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationRequest.FromString,
                    response_serializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationResponse.SerializeToString,
            ),
            'Classification': grpc.unary_unary_rpc_method_handler(
                    servicer.Classification,
                    request_deserializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationRequest.FromString,
                    response_serializer=arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arg_services.mining.v1.AduService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AduService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Segmentation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arg_services.mining.v1.AduService/Segmentation',
            arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationRequest.SerializeToString,
            arg__services_dot_mining_dot_v1_dot_adu__pb2.SegmentationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Classification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arg_services.mining.v1.AduService/Classification',
            arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationRequest.SerializeToString,
            arg__services_dot_mining_dot_v1_dot_adu__pb2.ClassificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
