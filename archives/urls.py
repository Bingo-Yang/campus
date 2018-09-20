#coding=utf-8
from django.conf.urls import url

from archives import views

urlpatterns = [
    url(r'^student/',views.stu_base),
    url(r'^start/',views.stu_start),
    url(r'^stu_up/(\d?)',views.stu_update),
    url(r'^select/',views.stu_select),
    url(r'^teacher/(\d?)',views.tea_base),
    url(r'^tea_up/',views.tea_update),
]