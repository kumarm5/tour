from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import NewsInfo

# Create your views here.
class News(TemplateView):
    def get(self, request, *args):
        news_details = NewsInfo.objects.filter(status=True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, self.template_name, {'news_details': news_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
