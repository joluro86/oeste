from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publicador
from .forms import PublicadorForm

class PublicadorListView(ListView):
    model = Publicador
    template_name = 'publicador_list.html'
    context_object_name = 'publicadores'

class PublicadorDetailView(DetailView):
    model = Publicador
    template_name = 'publicador_detail.html'
    context_object_name = 'publicador'

class PublicadorCreateView(CreateView):
    model = Publicador
    form_class = PublicadorForm
    template_name = 'publicador_form.html'
    success_url = reverse_lazy('publicador_list')

class PublicadorUpdateView(UpdateView):
    model = Publicador
    form_class = PublicadorForm
    template_name = 'publicador_form.html'
    success_url = reverse_lazy('publicador_list')

class PublicadorDeleteView(DeleteView):
    model = Publicador
    template_name = 'publicador_confirm_delete.html'
    success_url = reverse_lazy('publicador_list')


