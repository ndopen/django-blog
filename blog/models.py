from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class PublishedManager(models.Manager):
    '''定义published 模型管理方法，返回贴文状态为发布的对象'''
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')

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
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        '''规范绝对url'''
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    

class Comment(models.Model):
    '''Comment system models'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return f"comment by {self.name} on {self.post}"

    class Meat():
        ordering = ('created',)