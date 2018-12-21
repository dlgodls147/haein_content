from django.shortcuts import render, render_to_response
from bookmark.models import Bookmark
from anaconda_navigator.utils.py3compat import request

# Create your views here.

def home(request):
    #select * from bookmark_bookmark order by title ���� ����
    urlList = Bookmark.objects.order_by("title")
    #select count(*) from bookmark_bookmark ���� ����
    urlCount = Bookmark.objects.all().count()
    # list.html �丮������ �Ѿ�� ���
    return render_to_response("list.html", {"urlList" : urlList, "urlCount" : urlCount})

def detail(request):
    #get ������� ���� �޾ƿ���
    addr = request.GET["url"]
    #select * from bookmark_bookmark where url=.. �� �����
    dto = Bookmark.objects.get(url=addr)
    return render_to_response("detail.html", {"dto":dto})