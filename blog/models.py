from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PublisedManager(models.Manager):
    '''定义published 模型管理方法，返回贴文状态为发布的对象'''
    def get_queryset(self):
        return super(PublisedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):
    '''
    @Description	:Blog Post DataModels
    ----------
    @Param			:None
    ----------
    @Returns		:None
    '''
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED')
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    class Meat():
        ordering = ('-publish')

    def __str__(self):
        '''默认返回 title'''
        return self.title

    objects = models.Manager()
    published = PublisedManager()

