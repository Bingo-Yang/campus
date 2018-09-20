# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.db.models import Avg
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from database.models import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Create your views here.
def register(request):
    courses = Course.objects.all()
    if request.method == 'GET':
        return render(request,'register.html',{'course':courses})
    else:
        try:
            type1 = request.POST.get('type')
            name = request.POST.get('name')
            code = request.POST.get('code')
            cls = request.POST.get('cls')
            clz = Clazz.objects.get(cla_name=cls)
            print clz
            stu = Stu.objects.get(st_id=code, st_name=name,st_clazz=clz)
            if stu:
                for co in courses:
                    co1 = request.POST.get(co.cou_name)
                    StuCourse.objects.create(student=stu,cls=clz,course=co,sc_score=co1,sc_type=type1)
                return render(request, 'registery.html')
            else:
                return render(request, 'register.html', {'course': courses})
        except:
            return HttpResponse('输入的成绩不是数字')



def select(request):
    if request.method == 'GET':
        return render(request,'select.html')
    else:
        try:
            value = request.POST.get('type','')
            if value == '1':
                code = request.POST.get('condition','')
                codes = Stu.objects.get(st_id=code).stucourse_set.all()
                return render(request, 'select.html',{'codes':codes,'code':code})
            else:
                name = request.POST.get('condition','')
                codes = Stu.objects.get(st_name=name).stucourse_set.all()
                return render(request, 'select.html', {'codes': codes, 'code': name})
        except:
            return HttpResponse('输入有误')


def stat(request):
    clz = Clazz.objects.all()
    course = Course.objects.all()
    if request.method == 'GET':

        return render(request, 'stat.html',{'clz':clz,'course':course})
    else:
        cls = int(request.POST.get('cls',''))
        type = request.POST.get('type','')

        stus = Clazz.objects.get(cla_id=cls).stu_set.all()
        datas = {}
        for stu in stus:
            score = []
            data = StuCourse.objects.filter(student=stu,sc_type=type)
            it = 0
            for ds in data:
                st = ds.student.st_name
                a = ds.sc_score
                it += a
                score.append(a)
            score.append(it)
            datas[st] = score
        return render(request, 'stat.html', {'clz': clz,'datas':datas,'course':course,'type':type})



def grade(request):
    grades = Grade.objects.all()
    cour= Course.objects.all()
    if request.method == 'GET':
        return render(request, 'grade.html',{'grades':grades,'cour':cour})
    else:
        gra = request.POST.get('gr')
        type = request.POST.get('type')
        clazz = Grade.objects.get(gr_id=gra).clazz_set.all()
        datas = {}
        for clss in clazz:
            da = []
            clz = clss.cla_name
            # 学生人数
            counts = StuCourse.objects.filter(cls=clss).count()
            cr = cour.count()
            count = counts/cr
            da.append(count)
            #考试类型
            da.append(type)
            # 科目平均分
            su = 0
            for co in cour:
                cas = StuCourse.objects.filter(cls=clss,sc_type=type,course=co)
                lenth = cas.count()
                a = 0
                for c in cas:
                    c1 = c.sc_score
                    a += c1
                avg = a/lenth
                da.append(avg)
                su += a
            da.append(su)
            datas[clz] = da
        return render(request, 'grade.html', {'grades': grades,'cour':cour,'datas':datas})





code1 = None
def exist(request):
    code = request.POST.get('code','')
    global code1
    code1 = code
    count = Stu.objects.filter(st_id=code).count()

    if count == 1:
        return JsonResponse({'flag':True})
    else:
        return JsonResponse({'flag':False})


def exist1(request):
    name = request.POST.get('name', '')
    count = Stu.objects.filter(st_id=code1,st_name=name).count()
    if count == 1:
        return JsonResponse({'flag': True})
    else:
        return JsonResponse({'flag': False})

def exist2(request):
    name = request.POST.get('name', '')
    print name
    count = Clazz.objects.filter(cla_name=name).count()
    if count == 1:
        return JsonResponse({'flag': True})
    else:
        return JsonResponse({'flag': False})


# def exist3(request):
#     type1 = int(request.POST.get('a'))
#     con = request.POST.get('con')
#     print type1,con
#     # try:
#     if type1 == 1:
#         print 1
#         codes = Stu.objects.get(st_id=con).stucourse_set.all()
#         return render(request, 'select.html', {'codes': codes, 'code': con})
#     else:
#         codes = Stu.objects.get(st_name=con).stucourse_set.all()
#         return JsonResponse({'codes': codes})
#     # except:
#     #     return HttpResponse('输入有误')