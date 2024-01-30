from concurrent import futures
import time

import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def sayHello(self, request, context):
        print("SayHello Request Made")
        print(request)
        reply = greet_pb2.HelloReply()
        reply.message = f"{request.greeting} {request.name}"

        return reply

    def parrotSaysHello(self, request, context):
        print('parrotSaysHello Request Made')
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"

            yield hello_reply
            time.sleep(1)

    def chattyClientSaysHello(self, request_iterator, context):
        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print("chattyClientSaysHelloRequestMade:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages."
        return delayed_reply

    def interactingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello Request Made:")
            print(request)

            hello_reply = greet_pb2.HelloReply(message=f"{request.greeting} {request.name}")

            yield hello_reply


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:8000")
    server.start()
    server.wait_for_termination()
