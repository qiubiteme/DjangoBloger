from django.urls import path, re_path

from comment import views

app_name = 'comment'
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.posts_comment, name='posts_comment'),
]