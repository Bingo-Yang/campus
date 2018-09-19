#coding=utf-8
from django.conf.urls import url

from archives import views

urlpatterns = [
    url(r'^base/',views.stu_base),
    url(r'^start/',views.stu_start),
    url(r'^stu_up/',views.stu_update),
    url(r'^update/(\d?)',views.stu_update2),
]