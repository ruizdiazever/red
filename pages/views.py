from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Page
from django.urls import reverse_lazy


# See here https://ccbv.co.uk/ for more information, Ever.


# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#detailview
class PageDetailView(DetailView):
    model = Page

# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview
class PageListView(ListView):
    model = Page

# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'ordering']
    success_url = reverse_lazy('pages:pages')

# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')