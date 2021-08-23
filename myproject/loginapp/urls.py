from django.contrib import admin
from django.urls import path, include
from loginapp import views
urlpatterns = [
    path('index', views.studentlogin),
    path('teachers', views.teacherlogin),
    path('dashboard', views.dashboard),
    path('generateotp', views.generateotp),
    path('about', views.about),
    path('myprofile', views.myprofile),
]
