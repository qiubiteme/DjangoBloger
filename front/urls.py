from django.urls import path, re_path

from front import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^posts/(?P<posts_id>[0-9]+)/$', views.detail, name='detail'),
]
