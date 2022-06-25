from django.shortcuts import render

from Devices.models import Laptop

# Create your views here.
def index(request):
    laptop_list=Laptop.objects.all()
    laptops={
        'laptops':laptop_list
    }
    return render(request,'Devices/laptop-list.html',laptops)#'app_name/file.html'
