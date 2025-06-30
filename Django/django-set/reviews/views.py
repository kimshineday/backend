from django.shortcuts import render

# Create your views here.
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from rest_framework.views import APIView # as.view

# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        # 전체 모델 불러오기
        reviews = Review.objects.all()
        # 장고 객체를 json 형태로 변환
        serializer = ReviewSerializer(reviews, many=True) # 여러개 데이터가 있다는 것을 명시.

        return Response(serializer.data)
    
# api/v1/reviews/review_id [GET]
class ReviewID(APIView):
    def get(Self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
