# coding=utf-8
from django.conf.urls import url


import views

urlpatterns = [
    # 成绩录入
    url(r'^register/',views.register),
    # 成绩查询
    url(r'^select/',views.select),
    # 班级成绩统计
    url(r'^stat/',views.stat),
    # 年级成绩统计
    url(r'^grade/',views.grade),
    # AJAX
    url(r'^exist/',views.exist),
    url(r'^exist1/',views.exist1),
    url(r'^exist2/', views.exist2),
    # url(r'^exist3/', views.exist3),

]