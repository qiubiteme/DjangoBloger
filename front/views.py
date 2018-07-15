import markdown as markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView

from comment.forms import CommentForm
from comment.models import Comment
from front.models import Category, Posts


class IndexView(ListView):
    """ 首页的视图函数 """
    model = Posts
    template_name = 'front/index.html'
    context_object_name = 'posts_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 6


def detail(request, posts_id):
    """" 根据模板页传递的,id查询详情文章"""
    posts = get_object_or_404(Posts, pk=posts_id)
    #  markdown 模块支持,渲染详情页
    posts.content = markdown.markdown(posts.content,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

    # 获取这篇 post 下的全部评论
    comment_list = Comment.objects.filter(posts_id=posts.pk)

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'posts': posts,
               'comment_list': comment_list
               }
    # get请求是登录界面进入时发生
    if request.method == "GET":
        posts.increase_views()
        return render(request, 'front/detail.html', context=context)
    # post请求是提交登录表单的时候
    elif request.POST:
        content = request.POST.get('content')
        if context:
            comment = Comment(author=posts.users.nickname, email=posts.users.email,
                              content=content, created_time=timezone.now(), posts_id=posts.pk)
            comment.save()
            posts.increase_comment_num()

        # 重定向到评论的文章
        return render(request, 'front/detail.html', context=context)
