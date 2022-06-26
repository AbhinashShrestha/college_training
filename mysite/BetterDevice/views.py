from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DeleteView,UpdateView,DetailView

from BetterDevice.models import Laptop
# Create your views here.

class LaptopListView(ListView):
    model=Laptop
    BetterDevice='BetterDevice/laptop-list.httml'
    context_object_name='laptop'