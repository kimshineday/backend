from django.db import models
from common.models import CommonModel
# Create your models here.
class Review(CommonModel): # 만들어둔 모델 사용
    content = models.CharField(max_length=120) # 댓글
    likes_num = models.PositiveIntegerField(default=0) # 좋아요 기능
    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # 작성자
    feed = models.ForeignKey('feeds.Feed', on_delete=models.CASCADE) # 게시글
    # => 게시글에 달린 댓글들을 관리