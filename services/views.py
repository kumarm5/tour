from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ServicePage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'services.html', context={})