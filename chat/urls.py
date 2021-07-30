from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logs/', views.logs, name='logs'),
]