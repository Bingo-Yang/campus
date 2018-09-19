# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from database.models import *
# Create your views here.
def major(request):
    if request.session.get('uname','') == '管理员':
        majors = Major.objects.all().order_by('ma_id')
        if request.method == 'GET':

            return render(request,'major.html',{'majors':majors})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con',con})

def change(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request,'change.html',{'code':code,'name':name})
        else:
            code1 = int(request.POST.get('code',''))
            name1 = request.POST.get('name','')
            print code1,name1
            if code1 and name1:
                try:
                    Major.objects.filter(ma_id=code,ma_name=name).update(ma_id=code1,ma_name=name1)
                    return redirect('/maintain/major/')
                except:
                    con = '专业代码/专业名称已存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request,'power.html',{'con':con})
    else:
        Major.objects.filter(ma_id=code, ma_name=name).delete()
        return redirect('/maintain/major/')


def grade(request):
    if request.session.get('uname','') == '管理员':
        grades = Grade.objects.all().order_by('gr_id')
        if request.method == 'GET':
            return render(request,'grad.html',{'grades':grades})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con',con})

def change1(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request,'chang1.html',{'code':code,'name':name})
        else:
            code1 = int(request.POST.get('code',''))
            name1 = request.POST.get('name','')
            if code1 and name1:
                try:
                    Grade.objects.filter(gr_id=code,gr_name=name).update(gr_id=code1,gr_name=name1)
                    return redirect('/maintain/grade/')
                except:
                    con = '年级代码/年级名称已存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request,'power.html',{'con':con})
    else:
        Grade.objects.filter(gr_id=code, gr_name=name).delete()
        return redirect('/maintain/grade/')


def clazz(request):
    if request.session.get('uname','') == '管理员':
        cls = Clazz.objects.all().order_by('cla_id')
        if request.method == 'GET':
            return render(request,'cl.html',{'cls':cls})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request,'power.html',{'con',con})

def change2(request,code,name,gr,mj,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request,'change2.html',{'code':code,'name':name,'grade':gr,'major':mj})
        else:
            code1 = int(request.POST.get('code',''))
            name1 = request.POST.get('name','')
            gr1 = request.POST.get('grade','')
            mj1 = request.POST.get('major','')
            if code1 and name1 and gr and mj:
                try:
                    gr2 = Grade.objects.get(gr_name=gr1)
                    mj2 = Major.objects.get(ma_name=mj1)
                    Clazz.objects.filter(cla_id=code,cla_name=name).update(cla_id=code1,cla_name=name1,cla_grade=gr2,cla_major=mj2)
                    return redirect('/maintain/clazz/')
                except:
                    con = '班级代码/班级名称已存在/专业名称不存在/年级名称不存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request,'power.html',{'con':con})
    else:
        Clazz.objects.filter(cla_id=code, cla_name=name).delete()
        return redirect('/maintain/clazz/')





def course(request):
    if request.session.get('uname', '') == '管理员':
        courses = Course.objects.all().order_by('cou_id')
        if request.method == 'GET':
            return render(request, 'course.html', {'courses': courses})
    else:
        con = '对不起，你没有这项功能的权限。'
        return render(request, 'power.html', {'con', con})

def change3(request,code,name,id):
    id = int(id)
    if id == 1:
        if request.method == 'GET':
            return render(request,'change3.html',{'code':code,'name':name})
        else:
            code1 = int(request.POST.get('code',''))
            name1 = request.POST.get('name','')
            if code1 and name1:
                try:
                    Course.objects.filter(cou_id=code,cou_name=name).update(cou_id=code1,cou_name=name1)
                    return redirect('/maintain/course/')
                except:
                    con = '学科代码/学科名称已存在。'
                    return render(request, 'power.html', {'con': con})
            else:
                con = '输入不能为空。'
                return render(request,'power.html',{'con':con})
    else:
        Major.objects.filter(ma_id=code, ma_name=name).delete()
        return redirect('/maintain/course/')