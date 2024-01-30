import greet_pb2_grpc
import greet_pb2
import time
import grpc


def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting):")

        if name == "":
            break

        request = greet_pb2.HelloRequest(greeting="Hello", name=name)
        yield request
        time.sleep(1)


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        while True:
            print("1. sayHello - Unary")
            print("2. parrotSaysHello - Server Side Streaming")
            print("3. chattyClientSaysHello - Client Side Streaming")
            print("4. interactingHello - Both Streaming")
            print("0. exit")

            call_id = int(input("Which rpc would you like to call:"))

            match call_id:
                case 1:
                    hello_request = greet_pb2.HelloRequest(greeting="Hello", name="Server")
                    hello_reply = stub.sayHello(hello_request)
                    print("sayHello response Received:")
                    print(hello_reply)
                case 2:
                    hello_request = greet_pb2.HelloRequest(greeting="Hello", name="Server")
                    hello_replies = stub.parrotSaysHello(hello_request)

                    print("parrotSaysHello response recieved ")
                    for reply in hello_replies:
                        print(reply)

                case 3:
                    delayed_reply = stub.chattyClientSaysHello(get_client_stream_requests())
                    print("chattyClientSaysHello")
                    print(delayed_reply)
                case 4:
                    responses = stub.interactingHello(get_client_stream_requests())

                    for response in responses:
                        print("Interacting response received: ")
                        print(response)
                case 0:
                    break
                case _:
                    print(f"Incorrect rpc number {call_id}")
