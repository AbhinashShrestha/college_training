from django.shortcuts import redirect, render

from Devices.models import Laptop

# Create your views here.
def index(request):
    laptop_list=Laptop.objects.all()
    laptops={
        'laptops':laptop_list
    }
    return render(request,'Devices/laptop-list.html',laptops)#'app_name/file.html'

def delete(request,id):
    del_obj=Laptop.objects.get(id=id)
    del_obj.delete()
    return redirect('index')
