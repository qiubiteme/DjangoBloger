from django.contrib import admin

# Register your models here.
from front.models import Options, Users, Category, Posts, Comment, Tag

admin.site.register(Options)
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Tag)
admin.site.register(Comment)

