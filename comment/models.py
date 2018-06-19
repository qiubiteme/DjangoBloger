from django.db import models

# Create your models here.
from django.utils import timezone


class Comment(models.Model):
    """     用于记录文章评论信息 """

    # 作者
    author = models.CharField("评论用户", max_length=30)
    # 邮箱
    email = models.CharField("邮箱", max_length=50)
    # 创建时间
    created_time = models.DateTimeField("评论时间", default=timezone.now)
    # 内容
    content = models.CharField("内容", max_length=1000)
    # 上级评论
    parent_comment = models.ForeignKey(
        'self',
        verbose_name="上级评论",
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    # 是否展示,此条评论
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)

    # 一对多关系.一篇文章可以有多条评论
    posts = models.ForeignKey(
        'front.Posts',  # 关键在这里！！
        verbose_name='博文',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_time']
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'
