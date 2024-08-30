import grpc
import proxy_pb2
import proxy_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proxy_pb2_grpc.VideoCrawlingStub(channel)
        response = stub.Videos(proxy_pb2.SearchRequest(query='example search', limit=5))
        print("Found links:")
        for link in response.links:
            print(link)

if __name__ == '__main__':
    run()
    