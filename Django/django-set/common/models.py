from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # auto_now_add : 데이터 생성 시간을 현재 기준으로. (업데이트가 되어도 수정이 되지 않음)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 생성되는 시간 기준으로. (생성 후 업데이트가 되면 업데이트된 시간으로 변경)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 추상기반의 클래스, DB의 테이블에 위와 같은 갈럼이 추가되지 않음.