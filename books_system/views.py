# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


# 图书信息展示
from database.models import Book, Borrow, Stu


# 图书信息登记
def book_register_view(request):
    if request.method == 'GET':
        return render(request, 'books_register.html')
    else:
        bo_id = request.POST.get('book_code', '')
        bo_name = request.POST.get('book_name', '')
        bo_author = request.POST.get('book_author', '')
        bo_type = request.POST.get('book_type', '')
        bo_publisher = request.POST.get('book_publisher', '')
        bo_ptime = request.POST.get('book_time', '')
        bo_price = request.POST.get('book_price', '')
        bo_operator = request.POST.get('book_operator', '')
        bo_rukutime = request.POST.get('book_rukutime', '')
        bo_introduce = request.POST.get('book_introduce', '')
        bo_number = request.POST.get('book_number')
        Book.objects.create(bo_id=bo_id, bo_name=bo_name, bo_author=bo_author, bo_type=bo_type,
                                   bo_publisher=bo_publisher, bo_ptime=bo_ptime, bo_price=bo_price,
                                   bo_operator=bo_operator, bo_rukutime=bo_rukutime, bo_number=bo_number,
                            bo_introduce=bo_introduce)
        return render(request, 'books_register.html')


# 图书信息展示
def book_data_view(request):
    if request.method == 'GET':
        book = Book.objects.all().order_by('-bo_operator')
        return render(request, 'books_data.html', {'book': book})
    else:
        if request.POST.get('choice') == 'book_code':
            # 搜索值编号
            content = request.POST.get('content', '')
            if content:
                book = Book.objects.filter(bo_id=content).all()
                return render(request, 'books_data.html', {'book': book})
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_name':
            # 搜索值书名
            content = request.POST.get('content', '')
            # 搜索字段包含输入内容
            if content:
                book = Book.objects.filter(bo_name__contains=content).all()
                return render(request, 'books_data.html', {'book': book})
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_author':
            # 搜索值作者
            content = request.POST.get('content', '')
            if content:
                book = Book.objects.filter(bo_author=content).all()
                return render(request, 'books_data.html', {'book': book})
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_type':
            # 搜索值类型
            content = request.POST.get('content', '')
            if content:
                book = Book.objects.filter(bo_type__contains=content).all()
                return render(request, 'books_data.html', {'book': book})
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_all':
            book = Book.objects.all().order_by('-bo_operator')
            return render(request, 'books_data.html', {'book': book})


# 借阅信息登记
def borrow_register_view(request):
    if request.method == 'GET':
        return render(request, 'borrow_register.html')
    else:
        # 获取书的编码
        bo_id = request.POST.get('bo_id', '')
        # 获取书的对象
        book = Book.objects.grt(bo_id=bo_id)
        # 获取学生id
        stu_id = request.POST.get('stu_code', '')
        stu = Stu.objects.get(st_id=stu_id)
        # 获取借阅开始时间
        start_time = request.POST.get('start_time', '')
        # 获取归还时间
        end_time = request.POST.get('end_time', '')
        # 获取登记负责人
        registrar = request.POST.get('registrar', '')
        borrow = Borrow.objects.create(book=book, student=stu, start_time=start_time, end_time=end_time, registrar=registrar)
        if borrow:
            return HttpResponse('<script>alert("借阅成功!");location.href="/books_system/borrow_register/";</script>')
        return HttpResponse('<script>alert("借阅失败!");location.href="/books_system/borrow_register/";</script>')


# 借阅信息展示
def borrow_information_view(request):
    if request.method == 'GET':
        borrow = Borrow.objects.all().order_by('-start_time')
        return render(request, 'borrow_information.html', {'borrow': borrow})
    else:
        if request.POST.get('choice') == 'book_code':
            # 搜索值编号
            content = request.POST.get('content', '')
            if content:
                borrow = Borrow.objects.filter(book_id=content).all()
                print borrow
                if borrow:
                    return render(request, 'borrow_information.html', {'borrow': borrow})
                return HttpResponse('操作失败，返回上一页面,重新操作。')
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_name':
            # 搜索借阅时间
            content = request.POST.get('content', '')
            # 获取图书集合
            book_set = Book.objects.filter(bo_name__contains=content).all()
            print book_set
            borrow = []
            for bo in book_set:
                bo_id = bo.bo_id
                borrow_set = Borrow.objects.filter(book_id=bo_id).all()
                # print borrow_set
                borrow.append(borrow_set)
            print borrow
            return render(request, 'borrow_information1.html', {'borrow': borrow})
        elif request.POST.get('choice') == 'st_id':
            # 搜索学号
            content = request.POST.get('content', '')
            if content:
                borrow = Borrow.objects.filter(student_id=content).all()
                if borrow:
                    return render(request, 'borrow_information.html', {'borrow': borrow})
                return HttpResponse('操作失败，返回上一页面重新查询。')
            return HttpResponse('操作失败，返回上一页面。')
        elif request.POST.get('choice') == 'book_type':
            # 搜索值类型borrow
            content = request.POST.get('content', '')
            borrow = Book.objects.filter(bo_type__contains=content).all()
            return render(request, 'borrow_information.html', {'borrow': borrow})
        elif request.POST.get('choice') == 'borrow_all':
            borrow = Borrow.objects.all().order_by('-start_time')
            return render(request, 'borrow_information.html', {'borrow': borrow})
        return HttpResponse('操作失败，返回上一页面。')


# 修改图书信息
def alert_books_view(request, num):
    if request.method == 'GET':
        book = Book.objects.filter(bo_id=num)
        return render(request, 'alert_books.html', {'book': book})
    else:
        bo_type=request.POST.get('book_type','')
        bo_id=request.POST.get('book_id', '')
        bo_name=request.POST.get('book_name', '')
        bo_author=request.POST.get('book_author', '')
        bo_publisher=request.POST.get('book_publisher', '')
        bo_price=request.POST.get('book_price', '')
        bo_operator=request.POST.get('book_operator', '')
        bo_number=request.POST.get('book_number', '')
        Setbook(num,bo_type,bo_id,bo_name,bo_author,bo_publisher,bo_price,bo_operator,bo_number)
        return redirect('/books_system/book_data/')


def Setbook(num, bo_type, bo_id, bo_name, bo_author, bo_publisher, bo_price, bo_operator, bo_number):
    Book.objects.filter(bo_id=num).update(bo_type=bo_type, bo_id=bo_id,bo_name=bo_name, bo_author=bo_author,bo_publisher=bo_publisher,
                                          bo_price=bo_price, bo_operator=bo_operator, bo_number=bo_number)


