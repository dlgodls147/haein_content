from django.shortcuts import render, render_to_response
from bookmark.models import Bookmark
from anaconda_navigator.utils.py3compat import request

# Create your views here.

def home(request):
    #select * from bookmark_bookmark order by title 쿼리 실행
    urlList = Bookmark.objects.order_by("title")
    #select count(*) from bookmark_bookmark 쿼리 실행
    urlCount = Bookmark.objects.all().count()
    # list.html 페리이지로 넘어가서 출력
    return render_to_response("list.html", {"urlList" : urlList, "urlCount" : urlCount})

def detail(request):
    #get 방식으로 변수 받아오기
    addr = request.GET["url"]
    #select * from bookmark_bookmark where url=.. 이 실행됨
    dto = Bookmark.objects.get(url=addr)
    return render_to_response("detail.html", {"dto":dto})