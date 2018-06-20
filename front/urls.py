from django.urls import path, re_path

from front import views
app_name = 'front'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^posts/(?P<posts_id>[0-9]+)/$', views.detail, name='detail'),
    # re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
