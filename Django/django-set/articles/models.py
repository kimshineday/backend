from django.db import models
from common.models import CommonModel
# Create your models here.
class Article(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 추가
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # 테이블 연결, 유저 데이터 삭제 되면 글도 삭제하는지.
    
    def __str__(self):
        return self.title