# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        user = request.POST.get('name','')
        pwd = request.POST.get('password','')
        if user and pwd :
            users = User.objects.filter(user_name = user,user_pwd = pwd)
            if users:
                for use in users:
                    uid = use.id
                    if uid < 5:
                        # del request.session['uname']
                        request.session['uname'] = '管理员'
                        request.session.set_expiry(60 * 60 * 24 * 3)
                        return render(request, 'base.html')
                    else:
                        # del request.session['uname']
                        request.session['uname'] = user
                        request.session.set_expiry(60*60*24*3)
                        return render(request,'base.html')
            else:
                return render(request,'login1.html')
