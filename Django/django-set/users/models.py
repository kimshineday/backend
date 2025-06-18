from django.db import models
from django.contrib.auth.models import AbstractUser # 이미 장고에 있는 기능을 상속 받아 활용
# 부모가 가진 기능을 가져오고, 추가적으로 기능을 넣을 수 있다.

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField()
#     age = models.PositiveBigIntegerField(null=True)
#     gender = models.CharField(max_length=10)
    
#     def __str__(self):
#         return f'{self.name} / ({self.age}세)'

class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')
