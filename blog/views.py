# _*_ coding:utf-8 _*_
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

from .models import Blog, Category, Conment, Tagprofile

# 通用模块
tag_list = Tagprofile.objects.all()  # 标签云
category_list = Category.objects.all()  # 分类
article_rank = Blog.objects.all().order_by('-conment_nums')[:10]  # 热门博客
comment_list = Conment.objects.all().order_by('-add_time')[:20]  # 最新评论


class Index(View):
    """首页显示"""

    def get(self, request):
        article_list = Blog.objects.all().order_by('-edit_time')[:5]
        article_rank = Blog.objects.all().order_by('-conment_nums')[:5]

        return render(request, 'index.html', {
            'article_list': article_list,
            'article_rank': article_rank,
            'category_list': category_list,
            'tag_list': tag_list,
            'comment_list': comment_list,
        })


class About(View):
    """关于"""

    def get(self, request):
        return render(request, 'about.html', {
            'article_rank': article_rank,
            'category_list': category_list,
            'tag_list': tag_list,
            'comment_list': comment_list,
        })


class Articles(View):
    """博客文章"""

    def get(self, request, pk):
        if pk:
            category_obj = get_object_or_404(Category, id=pk)
            category = category_obj.name
            article_list = Blog.objects.filter(category_id=pk)
        else:  # pk=0时，获取全部列表
            article_list = Blog.objects.all()
            category = ''
        count = article_list.count()

        return render(request, 'articles.html', {
            'article_list': article_list,
            'category': category,
            'count': count,
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,

        })


class Archive(View):
    """归档"""

    def get(self, request):
        article_list = Blog.objects.all().order_by('-edit_time')

        return render(request, 'archive.html', {
            'article_list': article_list,
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,
        })


class Link(View):
    """链接"""

    def get(self, request):
        return render(request, 'link.html', {
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,
        })

    pass


class Message(View):
    """留言"""

    def get(self, request):
        return render(request, 'message_board.html', {
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,
        })


class Search(View):
    """搜索"""
    def get(self,request):
        key = request.GET.get('key','')
        if key:
            article_list = Blog.objects.filter(Q(title__icontains=key) | Q(content__icontains=key))

        else:
            article_list = ''
        count = article_list.count()
        return render(request,'search.html',{
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,
            'article_list':article_list,
            'count':count,
            'key':key,
        })


@csrf_exempt
def GetComment(request):
    """
    接收畅言的评论回推， post方式回推
    :param request:
    :return:
    """
    arg = request.POST
    data = arg.get('data')
    data = json.loads(data)
    title = data.get('title')
    url = data.get('url')
    source_id = data.get('sourceid')
    if source_id not in ['message']:
        article = Blog.objects.get(id=source_id)
        article.commenced()
    comments = data.get('comments')[0]
    content = comments.get('content')
    user = comments.get('user').get('nickname')
    Conment(title=title, source_id=source_id, user=user, url=url, conment=content).save()
    return JsonResponse({"status": "ok"})


class Detail(View):
    """博客详情页"""

    def get(self, request, pk):
        article = get_object_or_404(Blog, id=pk)
        return render(request, 'detail.html', {
            'article': article,
            'source_id': article.id,
            'tag_list': tag_list,
            'category_list': category_list,
            'article_rank': article_rank,
            'comment_list': comment_list,

        })


class Tagcloud(View):
    """标签云"""

    def get(self, request, id):
        tag = get_object_or_404(Tagprofile, id=id).tag_name
        article_list = Blog.objects.filter(tag__tag_name=tag)
        count = article_list.count()
        return render(request, 'tag.html', {
            'tag': tag,
            'article_list': article_list,
            'category_list': category_list,
            'tag_list': tag_list,
            'article_rank': article_rank,
            'comment_list': comment_list,
            'count': count,
        })


def page_not_look(request):
    """全局403配置"""
    from django.shortcuts import render_to_response
    response = render_to_response('403.html',{})
    response.status_code = 403
    return response

def page_not_found(request):
    """全局404配置"""
    from django.shortcuts import render_to_response
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response

def page_error(request):
    """全局500配置"""
    from django.shortcuts import render_to_response
    response = render_to_response('500.html',{})
    response.status_code = 500
    return response