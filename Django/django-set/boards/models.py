from django.db import models

# Create your models here.
# 게시글 구성 : 제목, 내용
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()