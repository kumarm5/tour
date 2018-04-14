from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *

# Create your views here.
class VisaTrack(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
        
    def post(self, request, *args, **kwargs):
        passport_num = request.POST.get('passport_num')
        passport_tracks = PassportTrack.objects.filter(passport_number = passport_num)
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'passport_tracks': passport_tracks })
        
class VisaLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-login.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
        