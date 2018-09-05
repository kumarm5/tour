from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from .models import *
from gallery.models import GalleryImages
from news.models import NewsInfo

# Create your views here.
class Gallery(TemplateView):
    def get(self, request, *args, **kwargs):
        gallery_id = int(self.kwargs['id'])
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_sub_cats = GallerySubCat.objects.filter(gallery_topic = gallery_id)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        return render(request, 'gallery.html', { 'gallery_sub_cats': gallery_sub_cats, 'gallery_menus': gallery_menus, 'tour_packages': tour_packages, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class GallerySubCatImage(TemplateView):
    def get(self, request, *args, **kwargs):
        cat_gallery_id = int(self.kwargs['id'])
        gallery_videos = GalleryVideos.objects.all()
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_sub_cat_images = GalleryImages.objects.filter(sub_category = cat_gallery_id)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        return render(request, self.template_name, { 'gallery_menus': gallery_menus, 'gallery_sub_cat_images': gallery_sub_cat_images, 'tour_packages': tour_packages, 'gallery_videos': gallery_videos, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
