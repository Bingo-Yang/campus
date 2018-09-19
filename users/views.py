# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from database.models import *
# Create your views here.
def register_user(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        pwd2 = request.POST.get('pwd2','')
        if pwd == pwd2:
            User.objects.create(user_name=uname,user_pwd=pwd)
            return HttpResponse('注册成功')
        else:
            return HttpResponse('ajax')


def select_user(request,num):
    if request.method == 'GET':
        if not num:
            return render(request, 'user_select.html')
        else:
            User.objects.filter(id=num).delete()
            return HttpResponse('删除成功')
    else:
        select = request.POST.get('select','')
        query = request.POST.get('query','')
        if select == '用户名':
            users = User.objects.filter(user_name=query)
            return render(request,'user_select.html',{'users':users})
        elif select == '用户编号':
            users = User.objects.filter(id=query)
            return render(request,'user_select.html',{'users':users})
        elif select == '所有用户':
            users = User.objects.all()
            return render(request, 'user_select.html', {'users': users})