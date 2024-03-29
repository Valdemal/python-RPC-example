# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greet_pb2 as greet__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sayHello = channel.unary_unary(
                '/greet.Greeter/sayHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.parrotSaysHello = channel.unary_stream(
                '/greet.Greeter/parrotSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.chattyClientSaysHello = channel.stream_stream(
                '/greet.Greeter/chattyClientSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.DelayedReply.FromString,
                )
        self.interactingHello = channel.stream_stream(
                '/greet.Greeter/interactingHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def parrotSaysHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def chattyClientSaysHello(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def interactingHello(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.sayHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'parrotSaysHello': grpc.unary_stream_rpc_method_handler(
                    servicer.parrotSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'chattyClientSaysHello': grpc.stream_stream_rpc_method_handler(
                    servicer.chattyClientSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.DelayedReply.SerializeToString,
            ),
            'interactingHello': grpc.stream_stream_rpc_method_handler(
                    servicer.interactingHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/sayHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def parrotSaysHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.Greeter/parrotSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def chattyClientSaysHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/greet.Greeter/chattyClientSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.DelayedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def interactingHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/greet.Greeter/interactingHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
