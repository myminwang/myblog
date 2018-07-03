# _*_ coding:utf-8 _*_

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """用户信息"""
    class Meta(object):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Blog(models.Model):
    """博客"""
    name = models.CharField(verbose_name='博客', max_length=50)
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(verbose_name='添加时间',default=datetime.now)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    image = models.ImageField(verbose_name='博客封面', upload_to='media/blog/%Y/%m')

    class Meta(object):
        verbose_name = '博客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Conment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='用户')
    conment = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(verbose_name='添加时间',default=datetime.now)

    class Meta(object):
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


