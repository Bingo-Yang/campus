# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta

import time

from database.models import *

# Create your views here.



def stu_base(request):
    if request.method == 'GET':
        clazzs = Clazz.objects.all()
        return render(request, 'student.html',{'clazzs':clazzs})
    else:
        #获取网页数据
        clazz = request.POST.get('clazz','')
        name = request.POST.get('name','')
        id = request.POST.get('id','')
        gender = request.POST.get('gender','')
        age = request.POST.get('age','')
        SFZ = request.POST.get('sfz','')
        birth = request.POST.get('birth','')
        phone = request.POST.get('phone','')
        addr = request.POST.get('addr','')
        political = request.POST.get('political','')
        nation = request.POST.get('nation','')
        #根据班级名称查询班级
        cla = Clazz.objects.get(cla_name=clazz)
        #存入学生表
        Stu.objects.create(st_id=id,st_name=name,st_gender=gender,st_age=age,st_SFZ=SFZ,st_birth=birth,st_phone=phone,st_addr=addr,st_political=political,st_nation=nation,st_clazz=cla)
        return HttpResponse('注册成功')

def stu_start(request):
    if request.method == 'GET':
        return render(request, 'stu_start.html')
    else:
        #如果点确定按钮
        if request.POST.get('submit','') == '确定':
            #根据获取的id查询学生信息并传入页面展示
            id = request.POST.get('id','')
            stu = Stu.objects.get(st_id=id)
            return render(request,'stu_start_2.html',{'stu':stu})
        #点提交获取数据存入数据库
        elif request.POST.get('submit', '') == '提交':
            sname = request.POST.get('name','')
            stu = Stu.objects.get(st_name=sname)
            clazz = stu.st_clazz
            starttime = request.POST.get('starttime','')
            startscore = request.POST.get('startscore','')
            StuRegister.objects.create(student=stu,clazz=clazz,start_score=startscore,start_time=starttime)
            return HttpResponse('提交成功')
        #点重置返回初始页
        elif request.POST.get('submit', '') == '重置':
            return render(request, 'stu_start.html')

def stu_update(request,num):
    if request.method == 'GET':
        #有参数走获取session
        if num:
            #获取session
            stu_str = request.session.get('stus')
            #删除session
            # del request.session['stus']
            #将字符串切成列表
            stu_list = stu_str.split(',')
            #遍历列表查出学生存进stus列表，传进网页
            stus = []
            #将num转为字符串
            num = long(num)
            for stu_name in stu_list:
                stu = Stu.objects.get(st_name=stu_name)
                stus.append(stu)
            return render(request,'stu_update.html',{'num':num,'stus':stus})
        else:
            return render(request, 'stu_update.html')
    #没有参数返回普通页面
    else:
        if request.POST.get('submit','') == '查询':
            select = request.POST.get('select','')
            query = request.POST.get('query','')
            if select == '学生编号':
                stus = Stu.objects.filter(st_id=query)
                #创建学生列表
                stu_list = []
                #循环遍历将学生姓名加入列表
                for stu in stus:
                    stu_list.append(stu.st_name)
                #把列表合成字符串
                stu_str = ','.join(stu_list)
                #把字符串存进session
                request.session['stus'] = stu_str
                return render(request, 'stu_update.html', {'stus': stus})
            elif select == '学生姓名':
                stus = Stu.objects.filter(st_name=query)
                # 创建学生列表
                stu_list = []
                # 循环遍历将学生姓名加入列表
                for stu in stus:
                    stu_list.append(stu.st_name)
                # 把列表合成字符串
                stu_str = ','.join(stu_list)
                # 把字符串存进session
                request.session['stus'] = stu_str
                return render(request, 'stu_update.html', {'stus': stus})
            elif select == '身份证号':
                stus = Stu.objects.filter(st_SFZ=query)
                # 创建学生列表
                stu_list = []
                # 循环遍历将学生姓名加入列表
                for stu in stus:
                    stu_list.append(stu.st_name)
                # 把列表合成字符串
                stu_str = ','.join(stu_list)
                # 把字符串存进session
                request.session['stus'] = stu_str
                return render(request, 'stu_update.html', {'stus': stus})
            elif select == '班级名称':
                stus = Clazz.objects.get(cla_name=query).stu_set.all()
                # 创建学生列表
                stu_list = []
                # 循环遍历将学生姓名加入列表
                for stu in stus:
                    stu_list.append(stu.st_name)
                # 把列表合成字符串
                stu_str = ','.join(stu_list)
                # 把字符串存进session
                request.session['stus'] = stu_str
                return render(request, 'stu_update.html', {'stus': stus})
        elif request.POST.get('submit','') == '提交':
            name = request.POST.get('name','')
            SFZ = request.POST.get('SFZ','')
            #获取生日字符串转为date格式
            birth_str = request.POST.get('birth','')
            birth = datetime.strptime(birth_str,'%Y-%m-%d')
            addr = request.POST.get('addr','')
            id = request.POST.get('id','')
            Stu.objects.filter(st_id=id).update(st_name=name,st_SFZ=SFZ,st_birth=birth,st_addr=addr)
            return HttpResponse('修改成功')


def stu_select(request):
    if request.method == 'GET':
        return render(request,'stu_select.html')
    else:
        #获取网页信息
        field = request.POST.get('field','')
        operator = request.POST.get('operator','')
        message = request.POST.get('message','')
        #根据学号查询
        if field == '学生编号':
            if operator == '大于':
                stus = Stu.objects.filter(st_id__gt=message)
                return render(request,'stu_select.html',{'stus':stus})
            elif operator == '小于':
                stus = Stu.objects.filter(st_id__lte=message)
                return render(request,'stu_select.html',{'stus':stus})
        elif field == '入学日期':
            message = datetime.strptime(message,'%Y-%m-%d')
            if operator == '大于':
                #把所有日期大于message的学生对象存入列表
                stus = []
                for stu in StuRegister.objects.filter(start_time__gt=message):
                    stus.append(stu.student)
                return render(request,'stu_select.html',{'stus':stus})
            elif operator == '小于':
                stus = []
                for stu in StuRegister.objects.filter(start_time__lte=message):
                    stus.append(stu.student)
                return render(request,'stu_select.html',{'stus':stus})
        elif field == '录取分数':
            if operator == '大于':
                stus = []
                for stu in StuRegister.objects.filter(start_score__gt=message):
                    stus.append(stu.student)
                return render(request,'stu_select.html',{'stus':stus})
            elif operator == '小于':
                stus = []
                for stu in StuRegister.objects.filter(start_score__lte=message):
                    stus.append(stu.student)
                return render(request,'stu_select.html',{'stus':stus})


def tea_base(request):
    if request.method == 'GET':
        majors = Major.objects.all()
        return render(request,'teacher.html',{'majors':majors})
    else:
        marriage = request.POST.get('marriage','')
        name = request.POST.get('name', '')
        id = request.POST.get('id', '')
        gender = request.POST.get('gender', '')
        age = request.POST.get('age', '')
        SFZ = request.POST.get('sfz', '')
        birth = request.POST.get('birth', '')
        phone = request.POST.get('phone', '')
        education = request.POST.get('education', '')
        political = request.POST.get('political', '')
        nation = request.POST.get('nation', '')
        major_name = request.POST.get('major','')
        major = Major.objects.get(ma_name=major_name)
        Teacher.objects.create(te_name=name,te_marriage=marriage,te_id=id,te_gender=gender,te_age=age,te_SFZ=SFZ,te_birth=birth,te_phone=phone,te_education=education,te_political=political,te_nation=nation,te_major=major)
        return HttpResponse('注册成功')


def tea_update(request,num):
    if request.method == 'GET':
        if num:
            teacher = Teacher.objects.get(te_id=num)
            return render(request,'tea_update2.html',{'teacher':teacher})
        else:
            return render(request, 'tea_update.html')
    else:
        if request.POST.get('submit','') == '查询':
            select = request.POST.get('select', '')
            query = request.POST.get('query', '')
            if select == '教师编号':
                teachers = Teacher.objects.filter(te_id=query)
                return render(request,'tea_update.html',{'teachers':teachers})
            elif select == '教师姓名':
                teachers = Teacher.objects.filter(te_name=query)
                return render(request,'tea_update.html',{'teachers':teachers})
            elif select == '专业名称':
                teachers = Major.objects.get(ma_name=query).teacher_set.all()
                return render(request,'tea_update.html',{'teachers':teachers})
        elif request.POST.get('submit','') == '修改':
            marriage = request.POST.get('marriage', '')
            name = request.POST.get('name', '')
            id = request.POST.get('id', '')
            gender = request.POST.get('gender', '')
            age = request.POST.get('age', '')
            SFZ = request.POST.get('sfz', '')
            birth_str = request.POST.get('birth', '')
            birth = datetime.strptime(birth_str, '%Y-%m-%d')
            phone = request.POST.get('phone', '')
            education = request.POST.get('education', '')
            political = request.POST.get('political', '')
            nation = request.POST.get('nation', '')
            major_name = request.POST.get('major', '')
            major = Major.objects.get(ma_name=major_name)
            Teacher.objects.filter(te_id=num).update(te_name=name, te_marriage=marriage, te_id=id, te_gender=gender, te_age=age,
                                   te_SFZ=SFZ, te_birth=birth, te_phone=phone, te_education=education,
                                   te_political=political, te_nation=nation, te_major=major)
            return HttpResponse('修改成功')