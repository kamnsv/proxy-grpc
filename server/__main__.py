from concurrent import futures
import grpc
import proxy_pb2_grpc

from videos import VideoCrawling

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proxy_pb2_grpc.add_VideoCrawlingServicer_to_server(VideoCrawling(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
