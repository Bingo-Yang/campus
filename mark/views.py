# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')


def select(request):
    return render(request,'select.html')


def stat(request):
    return render(request, 'stat.html')


def grade(request):
    return render(request, 'grade.html')