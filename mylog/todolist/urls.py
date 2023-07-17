from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
#      path('index/', views.index, name='index'),
      path('', views.loginUser, name='login'),
       path('logout/', views.logoutuser, name='logout'),
       path('task/', views.task, name='tasks'),
       path('todolist/', views.todolist, name='todolist')
 ]
