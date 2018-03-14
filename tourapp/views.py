from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics

# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        return render(request, 'home.html', context={ 'tour_packages': tour_packages })
