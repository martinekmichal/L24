from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import kontakt
from .forms import KontaktForm
from django.http import JsonResponse, FileResponse
from django.conf import settings
import os
from .mixins import LoggingMixin



def my_json(request):
    data = {
        'name': 'John Doe',
        'age': 'New York'
    }
    return JsonResponse(data)

def my_file_view(request):
    #file_path = os.path.join('path', 'to', 'your', 'file.pdf')
    filename = "test.txt"
    file_path = os.path.join(settings.MEDIA_ROOT, 'file', filename)
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='file.txt')
    return response

def my_image_view(request):
    #file_path = os.path.join('path', 'to', 'your', 'file.pdf')
    filename = "snehulak.jpg"
    file_path = os.path.join(settings.MEDIA_ROOT, 'img', filename)
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='image.jpg')
    return response

class KontaktListView(ListView, LoggingMixin):
    model = kontakt
    template_name = 'kontakt_list.html'

    def get(self, request, *args, **kwargs):
        self.log_action('View')
        return super().get(request, *args, **kwargs)

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

class KontaktUpdateView(UpdateView, LoggingMixin):
    model = kontakt
    form_class = KontaktForm
    template_name = 'kontakt_edit.html'
    success_url = reverse_lazy('kontakt_list')

    def form_valid(self, form):
        self.log_action('Update')
        return super().form_valid(form)