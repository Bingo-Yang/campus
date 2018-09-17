#coding=utf-8
from django.conf.urls import url

from teacher import views

urlpatterns = [
    url(r'^$',views.login),
    url(r'^base/',views.base),
    url(r'^t_manage/',views.t_manage),
    url(r'^t_course/',views.t_course),
    url(r'^t_master/',views.t_master),
    url(r'^select_teacher/',views.select_teacher),
    url(r'^select_master/',views.select_master)
]