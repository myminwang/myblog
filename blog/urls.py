#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "问道编程"
__date__ = "2018-07-04 14:45"

from django.urls import path

from .views import *

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('archive/', Archive.as_view(), name='archive'),
    path('link/', Link.as_view(), name='link'),
    path('message', Message.as_view(), name='message'),
    path('article/<int:pk>/', Articles.as_view(), name='article'),
    path('get_comment/', GetComment, name='get_comment'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('search/', Search.as_view(), name='search'),
    path('tag/<int:id>/', Tagcloud.as_view(), name='tag'),

]