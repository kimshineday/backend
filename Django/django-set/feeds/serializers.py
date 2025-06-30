from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer): 
    user = FeedUserSerializer(read_only=True) # feed의 user 모델을 직렬화
    review_set = ReviewSerializer(read_only=True, many=True)
    
    class Meta:
        model = Feed
        fields = '__all__'

        depth = 1 # 1로 설정할시 전체 정보 출력