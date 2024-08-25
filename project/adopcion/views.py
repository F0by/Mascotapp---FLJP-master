from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Adopcion
from .forms import AdopcionForm

class AdopcionList(ListView):
    model = Adopcion
    template_name = 'adopcion/lista_adopciones.html'  
    context_object_name = 'adopciones' 

class AdopcionDetail(DetailView):
    model = Adopcion
    template_name = 'adopcion/adopcion_detail.html'
    context_object_name = 'adopcion'

class AdopcionCreate(CreateView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopcion/adopcion_form.html'
    success_url = reverse_lazy('adopcion:adopcion_list')

class AdopcionUpdate(UpdateView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopcion/adopcion_form.html'
    success_url = reverse_lazy('adopcion:adopcion_list')

class AdopcionDelete(DeleteView):
    model = Adopcion
    success_url = reverse_lazy('adopcion:adopcion_list')