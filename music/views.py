from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Musique
from .forms import MusiqueForm

class MusiqueListView(ListView):
    model = Musique
    template_name = 'music/musique_list.html'
    context_object_name = 'musiques'

class MusiqueDetailView(DetailView):
    model = Musique
    template_name = 'music/musique_detail.html'
    context_object_name = 'musique'

class MusiqueCreateView(CreateView):
    model = Musique
    form_class = MusiqueForm
    template_name = 'music/musique_form.html'
    success_url = reverse_lazy('musique_list')

class MusiqueUpdateView(UpdateView):
    model = Musique
    form_class = MusiqueForm
    template_name = 'music/musique_form.html'
    success_url = reverse_lazy('musique_list')

class MusiqueDeleteView(DeleteView):
    model = Musique
    template_name = 'music/musique_confirm_delete.html'
    success_url = reverse_lazy('musique_list')
