from django.urls import include, path
from userapp import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
]