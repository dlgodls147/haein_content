from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
# ������ ����Ʈ���� Bookmark Ŭ������ � ������� ��µ��� �����ϴ� �ڵ�
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title","url")

#Bookmark Ŭ������ BookmarkAdmin Ŭ������ ����Ѵ�
admin.site.register(Bookmark, BookmarkAdmin)