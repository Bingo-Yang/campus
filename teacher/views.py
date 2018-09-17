# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')


def base(request):
    return render(request,'base.html')


def t_manage(request):
    return HttpResponse('111')


def t_course(request):
    return render(request,'course.html')


def t_master(request):
    return render(request,'master.html')


def select_teacher(request):
    return render(request,'select_teacher.html')


def select_master(request):
    return render(request,'select_master.html')