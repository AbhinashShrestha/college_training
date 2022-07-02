from django.contrib import admin
from django.urls import path
# from Devices import views
from Devices import views

urlpatterns = [
    # function base path
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('create',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
]