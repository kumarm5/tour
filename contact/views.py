from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo
from .models import *

# Create your views here.
class Contact(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        contact_information = ContactInformation.objects.last()
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'contact_information': contact_information, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class PreferredSalesAgentInfo(TemplateView):
    def get(self, request, *args, **kwargs):
        preferredsalesagents = PreferredSalesAgent.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'preferred-sales-agent.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'preferredsalesagents': preferredsalesagents, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
