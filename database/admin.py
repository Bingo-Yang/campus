# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from database.models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Clazz)
admin.site.register(Stu)
admin.site.register(Grade)
admin.site.register(Major)
admin.site.register(Teacher)
admin.site.register(TeacherCourse)
admin.site.register(StuCourse)
admin.site.register(HeadTeacher)
admin.site.register(StuRegister)
admin.site.register(Book)
admin.site.register(Borrow)
