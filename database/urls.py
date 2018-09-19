#coding=utf-8
from django.conf.urls import url

from database import views

urlpatterns = [
    url(r'^$',views.homepage),
]