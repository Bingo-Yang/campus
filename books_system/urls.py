#coding=utf-8
from django.conf.urls import url

from books_system import views

urlpatterns = [
    url(r'book_register/', views.book_register_view),
    url(r'book_data/', views.book_data_view),
    url(r'borrow_information/', views.borrow_information_view),
    url(r'borrow_register/', views.borrow_register_view),
    url(r'alter_books/?(\d+)', views.alert_books_view),
]
