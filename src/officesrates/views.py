from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from random import randint
from requests import post
from . import models 
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView


def offices_map(request):
    template_name='officesrates/index.html' 
    return render(request, template_name, {})

def offices_map_density(request):
    template_name='officesrates/kepler.html' 
    return render(request, template_name, {})

class OfficeList(TemplateView):
    template_name='officesrates/index.html' 
    model=models.Office
    def get_queryset(self):
        qs=self.model.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context