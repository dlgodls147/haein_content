from django.db import models

# Create your models here.
# ���̺��� �ʵ��� �ڷ����� ����
class Bookmark(models.Model):
    # �� ��� ����, null,null ��� ����
    title = models.CharField(max_length=100, blank=True, null=True)
    # unique �� �����̸Ӹ�Ű
    url = models.URLField("url", unique=True)
    # ��ü�� ���ڿ��� ǥ���ϴ� �Լ�
    def __str__(self):
        return self.title