from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *
# Create your views here.

class ForeignExchangePage(TemplateView):
    def get(self, request, *args, **kwargs):
        foreign_exchanges = ForeignExchange.objects.filter(status=True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'foreign-exchange.html', context= { 'foreign_exchanges': foreign_exchanges, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

class ForeignExchangeSendEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        foreignexchange_id = int(kwargs['id'])
        try:
            foreign_exchange = ForeignExchange.objects.get(id = foreignexchange_id)
        except:
            foreign_exchange = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)        
        return render(request, 'send-enquiry.html', context={ 'foreign_exchange': foreign_exchange, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
        