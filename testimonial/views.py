from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import Testimonial

# Create your views here.
class TestimonialPage(TemplateView):
    def get(self, request, *args, **kwargs):
        testimonials = Testimonial.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'testimonial.html', context={ 'testimonials': testimonials, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })