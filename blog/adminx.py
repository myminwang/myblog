#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "问道编程"
__date__ = "2018-07-03 16:47"

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import Blog, Conment, User



class BaseSetting(object):
    """
    后台修改需要的配置
    """
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSettings(object):
    """
    后台修改
    """
    site_title = '博客后台管理'
    site_footer = '博客后台管理'
    menu_style = 'accordion'  # 开启分组折叠


class BlogAdmin(object):
    list_display = ['name', 'content', 'add_time', 'click_nums']
    list_filter = ['name', 'content', 'click_nums']
    search_fields = ['name', 'content', 'add_time', 'click_nums']


class ConmentAdmin(object):
    list_display = ['user', 'conment', 'add_time']
    list_filter = ['user', 'conment']
    search_fields = ['user', 'conment', 'add_time']

# xadmin.site.register(User,UsersAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Conment, ConmentAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
