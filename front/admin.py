from django.contrib import admin

# Register your models here.
from front.models import Options, Users, Category, Posts, Comment, Tag


class OptionsAdmin(admin.ModelAdmin):
    list_display = ['options_name', 'options_describe']


admin.site.register(Options, OptionsAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'password', 'nickname', 'avatar', 'bio', 'status']


admin.site.register(Users, UsersAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'sort']


admin.site.register(Category, CategoryAdmin)


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'feature', 'create_time', 'revamp_time', 'status',
                    'comment_status', 'views', 'likes', 'comment_num', 'users', 'tag', 'comment', 'category', 'content']


admin.site.register(Posts, PostsAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']


admin.site.register(Tag, TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'created_time', 'content', 'parent_comment', 'is_enable']


admin.site.register(Comment, CommentAdmin)
