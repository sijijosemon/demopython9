
from django.contrib import admin
from django.urls import path, include
from .import views
from school.views import  get_courses

urlpatterns = [

    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('register1',views.register1,name="register1"),
    path('loggedin', views.loggedin, name="loggedin"),
    path('regform',views.regform,name="regform"),
    path('confirm',views.confirm,name='confirm'),
    path('logout',views.logout,name='logout'),
    path('get_courses/', get_courses, name='get_courses'),
]