from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView,DetailView
from django.core.paginator import Paginator
from BetterDevice.models import Laptop
# Create your views here.
from .forms import LaptopRegistration

class LaptopListView(ListView):
    model=Laptop
    template_name='BetterDevice/laptop-list.html'
    context_object_name='laptops'
    
    def get_context_data(self,*args ,**kwargs):
        laptops=self.get_queryset()#laptop is name of model
        paginator=Paginator(laptops,7)
        page_number=self.request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        context={'laptops':page_obj}
        return context
class LaptopCreateView(CreateView):
    form_class=LaptopRegistration
    template_name='BetterDevice/laptop-create.html'
    success_url=reverse_lazy('laptop-list')
