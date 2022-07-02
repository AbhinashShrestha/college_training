from django.contrib import admin
from django.urls import path
# from Devices import views
from BetterDevice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LaptopListView.as_view(),name='laptop-list'),
    path('create',views.LaptopCreateView.as_view(),name='laptop-create'),
]