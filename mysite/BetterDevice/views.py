# from re import template
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DeleteView,UpdateView,DetailView

from BetterDevice.models import Laptop
# Create your views here.

class LaptopListView(ListView):
    model=Laptop
    template_name='BetterDevice/laptop-list.html'
    context_object_name='laptops'
