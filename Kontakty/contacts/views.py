from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import kontakt
from .forms import KontaktForm
from django.views.generic import DeleteView
from django.views.generic import UpdateView


class KontaktListView(ListView):
    model = kontakt
    template_name = 'kontakt_list.html'

class KontaktDetailView(DetailView):
    model = kontakt
    template_name = 'kontakt_detail.html'

class KontaktCreateView(CreateView):
    model = kontakt
    form_class = KontaktForm
    template_name = 'kontakt_create.html'
    success_url = reverse_lazy('kontakt_list')

class KontaktDeleteView(DeleteView):
    model = kontakt
    template_name = 'kontakt_delete.html'
    success_url = reverse_lazy('kontakt_list')

class KontaktUpdateView(UpdateView):
    model = kontakt
    form_class = KontaktForm
    template_name = 'kontakt_edit.html'
    success_url = reverse_lazy('kontakt_list')