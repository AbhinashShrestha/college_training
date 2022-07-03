from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('register/',views.register,name="register"),
]