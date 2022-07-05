from django.urls import path
from userapp import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name='logout'),
    path("password_reset/",views.password_reset_request,name="password_reset")
]