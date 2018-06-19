from django import template

from front.models import Posts, Category

register = template.Library()


@register.simple_tag
def get_hot_posts(num=5):
    """ 侧边栏最热门浏览,5篇文章列表 ,按浏览,排序"""
    return Posts.objects.all().order_by('views')[:num]


@register.simple_tag
def get_hot_comment_posts(num=5):
    """ 侧边栏最热门评论,5篇文章列表 ,按评论条数,排序"""
    return Posts.objects.all().order_by('comment_num')[:num]

@register.simple_tag
def get_hot_comment_posts(num=5):
    """ 侧边栏最热门点赞,5篇文章列表 ,按点赞,排序"""
    return Posts.objects.all().order_by('likes')[:num]

@register.simple_tag
def get_category_list():
    """ 获取文章的分类列表"""
    return Category.objects.all()
