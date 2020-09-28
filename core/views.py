from django.views.generic.base import TemplateView
from django.shortcuts import render

# See here https://ccbv.co.uk/ for more information, Ever.


# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/#django.views.generic.base.TemplateView
class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title' : "Ever Toujours"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
