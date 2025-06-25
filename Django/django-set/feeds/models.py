from django.db import models

# Create your models here.
from common.models import CommonModel

# 제목(title), 내용(content), 작성자(user)
# Feed와 User의 관계
# User -> Feed, Feed, Feed O
# Feed -> User, User, User X
# => User : Feed = 1 : n 

class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # user DB에서 가져옴. 유저 데이터가 삭제 되면 게시글도 삭제.
