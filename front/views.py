import markdown as markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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




def detail(request,posts_id):
    """" 根据模板页传递的,id查询详情文章"""
    posts = get_object_or_404(Posts, pk=posts_id)
    #  markdown 模块支持,渲染详情页
    posts.content = markdown.markdown(posts.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'front/detail.html', context={'posts': posts})

