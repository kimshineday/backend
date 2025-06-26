from rest_framework.serializers import ModelSerializer
from .models import User

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Feed에서 노출 시킬 정보들.
class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__' # 전체
        fields = ('username', 'email', 'is_superuser') # 유저 정보 이것만 보이게 설정 ## 필터링
            