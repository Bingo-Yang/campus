# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20,unique=True)
    user_pwd = models.CharField(max_length=20)
    def __unicode__(self):
        return u'用户:%s'%self.user_name

    class Meta:
        db_table = 't_user'

#课程表
class Course(models.Model):
    #课程代码
    cou_id = models.PositiveIntegerField(primary_key=True,unique=True)
    cou_name = models.CharField(max_length=20,unique=True)

    def __unicode__(self):
        return r'course:%s'%self.cou_name

    class Meta:
        db_table = 't_course'

# 年级表
class Grade(models.Model):
    # 年级代码
    gr_id = models.PositiveIntegerField(unique=True,primary_key=True)
    gr_name = models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return u'年级:%s'%self.gr_name

    class Meta:
        db_table = 't_grade'

# 专业表
class Major(models.Model):
    ma_id = models.PositiveIntegerField(unique=True,primary_key=True)
    ma_name = models.CharField(max_length=20, unique=True)
    def __unicode__(self):
        return u'专业:%s'%self.ma_name

    class Meta:
        db_table = 't_major'

# 班级表
class Clazz(models.Model):
    cla_id = models.PositiveIntegerField(primary_key=True)
    cla_name = models.CharField(max_length=20)
    # 年级
    cla_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    # 专业
    cla_major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'班级:%s' % self.cla_name

    class Meta:
        db_table = 't_clazz'

# 学生表
class Stu(models.Model):
    # 学生编号
    st_id = models.PositiveIntegerField(primary_key=True,unique=True)
    st_name = models.CharField(max_length=10)
    st_gender = models.CharField(max_length=10)
    st_age = models.PositiveIntegerField()
    # 民族
    st_nation = models.CharField(max_length=10)
    # 政治面貌
    st_political = models.CharField(max_length=10)
    st_birth = models.DateField(auto_now_add=True)
    # 身份证
    st_SFZ = models.CharField(max_length=20)
    # 电话
    st_phone = models.PositiveIntegerField()
    st_addr = models.TextField()
    st_clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'学生:%s' % self.st_name

    class Meta:
        db_table = 't_stu'

# 教师表
class Teacher(models.Model):
    # 教师编号
    te_id = models.PositiveIntegerField(unique=True,primary_key=True)
    te_name = models.CharField(max_length=10)
    te_gender = models.CharField(max_length=10)
    te_age = models.PositiveIntegerField()
    # 民族
    te_nation = models.CharField(max_length=10)
    # 婚否
    te_marriage = models.CharField(max_length=10)
    # 政治面貌
    te_political = models.CharField(max_length=10)
    te_birth = models.DateField(auto_now_add=True)
    # 身份证
    te_SFZ = models.PositiveIntegerField()
    # 学历
    te_education = models.CharField(max_length=20)
    # 电话
    te_phone = models.PositiveIntegerField()
    te_major = models.ForeignKey(Major,on_delete=models.CASCADE)
    work_content = models.TextField()
    def __unicode__(self):
        return u'教师:%s'%self.te_name

    class Meta:
        db_table = 't_teacher'

# 教师任课表
class TeacherCourse(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher)
    course = models.ForeignKey(Course)
    rkDATE = models.DateField(auto_now_add=True)
    lizhiDATE = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return u'教师:%s,课程:%s'%(self.teacher.te_name,self.course.cou_name)

    class Meta:
        db_table = 't_teacherCourse'

# 学生课程成绩表
class StuCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Stu,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    sc_score = models.DecimalField(max_digits=4,decimal_places=1)
    sc_type = models.CharField(max_length=20)
    def __unicode__(self):
        return u'学生:%s,成绩:%s'%(self.student.st_name,self.course.cou_name)

    class Meta:
        db_table = 't_stuCourse'

# 班主任表
class HeadTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    clazz = models.OneToOneField(Clazz,on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    def __unicode__(self):
        return u'班主任:%s班级:%s'%(self.teacher.te_name,self.clazz.cla_name)

    class Meta:
        db_table = 't_headTeacher'

# 学生入学登记表
class StuRegister(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(Stu)
    clazz = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    start_score = models.PositiveIntegerField()
    start_time = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return u'学生登记:%s'%self.student.st_name

    class Meta:
        db_table = 't_stuRegister'

#图书信息表
class Book(models.Model):
    bo_id = models.PositiveIntegerField(primary_key=True,unique=True)
    bo_name = models.CharField(max_length=30)
    bo_price = models.DecimalField(max_digits=6,decimal_places=2)
    bo_type = models.CharField(max_length=20)
    #出版社
    bo_publisher = models.CharField(max_length=30)
    #作者
    bo_author = models.CharField(max_length=20)
    #简介
    bo_introduce = models.TextField()
    # 出版日期
    bo_ptime = models.DateField(auto_now_add=True)
    #操作员
    bo_operator = models.CharField(max_length=20)
    #入库日期
    bo_rukutime = models.DateField(auto_now_add=True)
    #入库数量
    bo_number = models.PositiveIntegerField()


    def __unicode__(self):
        return u'图书:%s' % self.bo_name

    class Meta:
        db_table = 't_book'

#借阅表
class Borrow(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Stu,on_delete=models.CASCADE)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'图书:%s,借阅人:%s' % (self.book.bo_name,self.student.st_name)

    class Meta:
        db_table = 't_borrow'
















