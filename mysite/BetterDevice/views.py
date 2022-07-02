from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DeleteView,UpdateView,DetailView
from django.core.paginator import Paginator
from BetterDevice.models import Laptop
# Create your views here.

class LaptopListView(ListView):
    model=Laptop
    template_name='BetterDevice/laptop-list.html'
    context_object_name='laptops'
    
    def get_context_data(self,*args ,**kwargs):
        laptop=self.get_queryset()#laptop is name of model
        paginator=Paginator(laptop,5)
        page_number=self.request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        context={'laptop':page_obj}
        return context
