# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Index(View):
    """首页显示"""
    def get(self,request):

        return render(request,'index.html',{})