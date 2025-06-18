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
    
    def __str__(self):
        return self.title