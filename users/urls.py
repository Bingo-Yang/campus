#coding=utf*8
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^register/',views.register_user),
    url(r'^select/(\d?)',views.select_user),
]