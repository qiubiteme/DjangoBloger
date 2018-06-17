from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Category, Posts


def index(request):
    # 拿到所有分类
    category_lsit = Category.objects.all()
    # 所有文章列表
    posts_list = Posts.objects.all()
    context = {'category_lsit': category_lsit, 'posts_list': posts_list}
    print(posts_list)

    return render(request, 'front/index.html', context)
