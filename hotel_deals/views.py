from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo
from .models import *

# Create your views here.
class Cities(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        cities_details = City.objects.all()
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'cities.html', context={ 'tour_packages': tour_packages, 'cities_details': cities_details, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class Hotels(TemplateView):
    def get(self, request, **kwargs):
        city_id = int(kwargs['id'])
        hotel_details = Hotel.objects.filter(city = city_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'hotels.html', context={ 'tour_packages': tour_packages, 'hotel_details': hotel_details, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class HotelInfo(TemplateView):
    def get(self, request, **kwargs):
        hotel_id = int(kwargs['id'])
        hotel_details = HotelDetails.objects.get(hotel = hotel_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'hotel-details.html', context= { 'hotel_details': hotel_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
