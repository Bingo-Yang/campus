from django.conf.urls import url

from sysmessage import views

urlpatterns=[
    url(r'^$',views.dologin)
]