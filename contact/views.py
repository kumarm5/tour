from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *

# Create your views here.
class Contact(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
 
class PreferredSalesAgentInfo(TemplateView):
    def get(self, request, *args, **kwargs):
        preferredsalesagents = PreferredSalesAgent.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'preferred-sales-agent.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'preferredsalesagents': preferredsalesagents })
