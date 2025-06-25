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
        print(serializer)

        return Response(serializer.data)
    