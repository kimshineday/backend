from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    age = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=10)
    