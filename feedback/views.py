from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedback
from django.contrib import messages
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo

# Create your views here.

class FeedbackHome(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'feedback.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        messages.success(request, 'Thank you for your feedback.')
        feedback = Feedback.objects.create(name=username, mobile_number=mobile, message=message, rating=rating)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]

        return render(request, 'feedback.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
