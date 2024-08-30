import grpc
import proxy_pb2
import proxy_pb2_grpc
from youtubesearchpython import VideosSearch

class VideoCrawling(proxy_pb2_grpc.VideoCrawlingServicer):

    def Videos(self, request:proxy_pb2.SearchRequest, 
               context:grpc.ServicerContext) -> proxy_pb2.SearchResponse:

        videos_search = VideosSearch(request.query, limit=request.limit)
        results = videos_search.result()['result']
                
        video_links = []
        for video in results:
            video_links.append(video['link'])
            
        return proxy_pb2.SearchResponse(links=video_links)    
