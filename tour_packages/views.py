from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *

# Create your views here.
class Tour(TemplateView):
    def get(self, request, **kwargs):
        tour_topic_id = int(kwargs['id'])
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_details = Tours.objects.filter(tour_topic_id = tour_topic_id)
        return render(request, 'tour.html', context={ 'tour_packages': tour_packages, 'tour_details': tour_details, 'gallery_menus': gallery_menus })

class Packages(TemplateView):
    def get(self, request, **kwargs):
        tour_id = int(kwargs['id'])        
        tour_package_details = TourPackages.objects.filter(tour = tour_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        return render(request, 'package.html', context={ 'tour_packages': tour_packages, 'tour_package_details': tour_package_details, 'gallery_menus': gallery_menus })

class PackageInfo(TemplateView):
    def get(self, request, **kwargs):
        package_id = int(kwargs['id'])
        package_details = PackageDetails.objects.get(package = package_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        return render(request, 'package-details.html', context= { 'package_details': package_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
        