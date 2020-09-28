from django.urls import path
from . import views
from pages.views import PageListView, PageDetailView, PageCreate#, PageDelete

pages_patterns = ([
        path('', PageListView.as_view(), name='pages'),
        path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name="page"),
        path('create/', PageCreate.as_view(), name='create'),
        #path('delete/', PageDelete.as_view(), name='delete'),

], 'pages')
