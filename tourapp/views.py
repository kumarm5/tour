from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from testimonial.models import Testimonial
from insurance.models import Insurance
from news.models import NewsInfo
from .models import HomeImageSlider, About

# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        new_infos = NewsInfo.objects.all()

        homeimagesliders = HomeImageSlider.objects.filter(status=True)

        about = About.objects.filter(status = True).last()

        testimonial_details = Testimonial.objects.all()
        try:
            insurance_details = Insurance.objects.latest('id')
        except:
            insurance_details = None

        return render(request, 'home.html', context={ 'homeimagesliders': homeimagesliders, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'testimonial_details': testimonial_details, 'insurance_details': insurance_details, 'new_infos': new_infos, 'footer_news': footer_news, 'footer_galleries': footer_galleries, 'about': about })

# class Contact(TemplateView):
#     def get(self, request, **kwargs):
#         tour_packages = Topics.objects.filter(status = True)
#         gallery_menus = GalleryMenu.objects.filter(status = True)
#         return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
 