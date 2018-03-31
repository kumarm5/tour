from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from testimonial.models import Testimonial
from insurance.models import Insurance

# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        testimonial_details = Testimonial.objects.all()
        insurance_details = Insurance.objects.latest('id')
        return render(request, 'home.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'testimonial_details': testimonial_details, 'insurance_details': insurance_details })

class Contact(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
 