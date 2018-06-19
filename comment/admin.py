from django.contrib import admin

# Register your models here.
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'created_time', 'content', 'parent_comment', 'is_enable']


admin.site.register(Comment, CommentAdmin)