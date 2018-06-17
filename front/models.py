from django.db import models

# Create your models here.
from django.utils import timezone


class Options(models.Model):
    """     用于记录网站的一些配置属性信息，如：站点标题，站点描述等    """
    # 字符串字段
    keystering = models.CharField(unique=True, max_length=200)
    # JSON字段
    valuestreing = models.TextField()

    class Meta:
        verbose_name = "站点描述"
        verbose_name_plural = verbose_name


class Users(models.Model):
    """  用户表   用于记录用户信息        """
    user_name = models.CharField("用户名", max_length=200, blank=True)
    # URL 别名
    # slug = models.CharField("用户首页", max_length=200)
    # 邮箱或者登录名
    email = models.EmailField("邮箱", unique=True)
    # 密码字段
    password = models.CharField("密码", max_length=200)
    # 昵称
    nickname = models.CharField("昵称", max_length=100, blank=True)
    # 头像地址
    avatar = models.CharField("头像地址", max_length=200, blank=True)  # 这里可以用url后续改
    # 用户简介
    bio = models.CharField("自我介绍", max_length=500, blank=True)
    # 用户是否邮箱激活
    status = models.BooleanField("邮箱激活状态")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "用户名"
        verbose_name_plural = verbose_name


class Category(models.Model):
    """  文章分类表   用于记录文章分类信息       """
    # 分类的url
    # slug = models.CharField("分类url", unique=True, max_length=200)
    # 分类名称
    category_name = models.CharField("分类名称", max_length=30, unique=True)
    sort = models.IntegerField("分类排序", default=0)

    def __str__(self):
        return self.category_name

    # 分类默认按,序号排序,
    class Meta:
        ordering = ['sort']
        verbose_name = "分类名称"
        verbose_name_plural = verbose_name


class Posts(models.Model):
    """ 文用户章模型 """
    # 文章状态
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    # 文章评论状态
    COMMENT_STATUS = (
        ('o', '打开'),
        ('c', '关闭'),
    )
    """ 文章表,用于记录文章信息     """
    # 文章的url
    # slug = models.CharField("文章地址", unique=True, max_length=200)
    #  文章标题
    title = models.CharField("标题", max_length=200)
    # 文章图片 URL 路径
    feature = models.CharField("图片地址", max_length=200, null=True)
    # 文章创建时间,auto_now_add.设置为当前时间,且不可更改,暂时改为,可修改
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    # 文章修改时间,auto_now 字段,不可修改
    revamp_time = models.DateTimeField("修改时间", auto_now=True)
    # 文章的状态,发表与草稿
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    # 文章评论状态,默认可评论
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')
    # 文章内容字段
    content = models.TextField("正文", blank=True, null=True)
    # 文章浏览次数,默认为 0
    views = models.PositiveIntegerField('浏览量', default=0)
    # 点赞次数
    likes = models.PositiveIntegerField("点赞", default=0)
    # 评论次数
    comment_num = models.PositiveIntegerField("评论次数", default=0)
    # 一对多关系,一个用户可以有多篇文章
    users = models.ForeignKey(
        'Users',  # 关键在这里！！
        verbose_name='文章作者',
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        'Tag',  # 关键在这里！！
        verbose_name='标签',
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(
        'Comment',  # 关键在这里！！
        verbose_name='评论',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # 文章所属分类,一对多关系,一篇文章可以属于多个分类,
    category = models.ForeignKey(
        "Category",
        verbose_name='文章分类',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'create_time'


class Tag(models.Model):
    """文章标签,用于seo,的处理"""
    name = models.CharField('标签', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """     用于记录文章评论信息 """

    # 作者
    author = models.CharField("评论用户", max_length=30)
    # 邮箱
    email = models.CharField("邮箱", max_length=50)
    # 创建时间
    created_time = models.DateTimeField("评论时间", default=timezone.now())
    # 内容
    content = models.CharField("内容", max_length=1000)
    # 上级评论
    parent_comment = models.ForeignKey(
        'self',
        verbose_name="上级评论"
        , on_delete=models.CASCADE)
    # 是否展示,此条评论
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)

    # 一对多关系.一篇文章可以有多条评论

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_time']
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'
