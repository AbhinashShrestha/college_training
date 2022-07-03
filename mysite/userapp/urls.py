from django.urls import path
from userapp import views

urlpatterns = [
    path('user-register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
]