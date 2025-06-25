from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer): 
    user = FeedUserSerializer() # feed의 user 모델을 직렬화
    class Meta:
        model = Feed
        fields = '__all__'

        depth = 1 # 1로 설정할시 전체 정보 출력