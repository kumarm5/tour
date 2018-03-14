from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from .models import *

# Create your views here.
class Tour(TemplateView):
    def get(self, request, **kwargs):
        tour_id = int(kwargs['id'])        
        tour_packages = Topics.objects.filter(status = True)
        tour_details = Tours.objects.filter(tour_topic_id = tour_id)
        return render(request, 'tour.html', context={ 'tour_packages': tour_packages, 'tour_details': tour_details })
