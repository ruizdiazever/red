from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Page
from django.urls import reverse_lazy


class PageDetailView(DetailView):
    model = Page

class PageListView(ListView):
    model = Page

class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'ordering']
    success_url = reverse_lazy('pages:pages')

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')