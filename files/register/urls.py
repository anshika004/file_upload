from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path("",views.register_index,name='home'),
    path("login/",views.loginUser,name='login'),
    path("logout/",views.logoutUser,name='logout'),
]    