from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *

# Create your views here.

class CabRentalCities(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        cities = Cities.objects.all()
        return render(request, 'cab-rental-cities.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'cities': cities })

