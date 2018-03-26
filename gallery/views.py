from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class Gallery(TemplateView):
    def get(self, request, *args, **kwargs):
        gallery_id = int(self.kwargs['id'])
        gallery_menus = GalleryMenu.objects.filter(status = True)
        gallery_sub_cats = GallerySubCat.objects.filter(gallery_topic = gallery_id)
        return render(request, 'gallery.html', { 'gallery_sub_cats': gallery_sub_cats, 'gallery_menus': gallery_menus})

class GallerySubCatImage(TemplateView):
    def get(self, request, *args, **kwargs):
        cat_gallery_id = int(self.kwargs['id'])
        gallery_menus = GalleryMenu.objects.filter(status = True)
        gallery_sub_cat_images = GalleryImages.objects.filter(sub_category = cat_gallery_id)        
        return render(request, self.template_name, { 'gallery_menus': gallery_menus, 'gallery_sub_cat_images': gallery_sub_cat_images })
