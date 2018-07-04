# _*_ coding:utf-8 _*_

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """用户信息"""
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Category(models.Model):
    """博客分类"""
    name = models.CharField(verbose_name='文档分类',max_length=20)
    add_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)
    edit_time = models.DateTimeField(verbose_name='修改时间',default=datetime.now)

    class Meta:
        verbose_name = '文档分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tagprofile(models.Model):
    tag_name = models.CharField('标签名', max_length=30)

    class Meta:
        verbose_name = '标签名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    """博客文章"""
    title = models.CharField(verbose_name='博客文章', max_length=50,default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,verbose_name='文章分类')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    digest = models.TextField(verbose_name='摘要',default='')
    add_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)
    edit_time = models.DateTimeField(verbose_name='更新时间',default=datetime.now)
    read_nums = models.IntegerField(verbose_name='阅读数', default=0)
    conment_nums = models.IntegerField(verbose_name='评论数', default=0)
    image = models.ImageField(verbose_name='博客封面', upload_to='blog/%Y/%m')
    tag = models.ManyToManyField(Tagprofile)


    class Meta:
        verbose_name = '博客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Conment(models.Model):
    """对博客评论"""
    user = models.CharField(verbose_name='评论用户', max_length=25)
    title = models.CharField(verbose_name="标题", max_length=100)
    source_id = models.CharField(verbose_name='文章id或source名称', max_length=25)
    conment = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(verbose_name='添加时间',default=datetime.now)
    url = models.CharField(verbose_name='链接', max_length=100)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



class Message(models.Model):
    """留言"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='用户')
    message = models.TextField(verbose_name='留言')
    add_time = models.DateTimeField(verbose_name='时间',default=datetime.now)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message
