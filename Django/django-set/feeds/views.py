from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def show_feed(request):
    return HttpResponse("show feed")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f'feed_id : {feed_id}, feed_content : {feed_content}')

def all_feed(request):
    return HttpResponse('all feed')
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializer

class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all()

        # 객채 -> JSON 시리얼라이저화
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        # Feed.objects.create() # 시리얼라이저에서 구현
        # 역직렬화 (클라이언트가 보내준 Json -> object)
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid(): # 토큰 인증
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            # print('post serializer'. serializer) # 로그 기록 남기기 -> 오류 있음

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        # feed는 현재 object, -> json -> Serialier
        serializer = FeedSerializer(feed)
        # print(serializer)

        return Response(serializer.data)
    