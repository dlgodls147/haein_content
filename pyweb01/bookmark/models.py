from django.db import models

# Create your models here.
# 테이블의 필드명과 자료형을 정의
class Bookmark(models.Model):
    # 빈값 허용 여부, null,null 허용 여부
    title = models.CharField(max_length=100, blank=True, null=True)
    # unique 는 프라이머리키
    url = models.URLField("url", unique=True)
    # 객체를 문자열로 표현하는 함수
    def __str__(self):
        return self.title