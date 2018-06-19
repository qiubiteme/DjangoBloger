from django.forms import forms, ModelForm

from comment.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'created_time', 'content','parent_comment']