from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from .models import *
from django.contrib import messages
# Create your views here.

class ForeignExchangePage(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            term_and_cond = TermsAndCondition.objects.last()
        except:
            term_and_cond = None

        foreign_exchanges = ForeignExchange.objects.filter(status=True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'foreign-exchange.html', context= { 'foreign_exchanges': foreign_exchanges, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond })

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
        
    def post(self, request, *args, **kwargs):
        foreignexchange_id = int(kwargs['id'])
        try:
            foreign_exchange = ForeignExchange.objects.get(id = foreignexchange_id)
        except:
            foreign_exchange = None

        username = request.POST.get('username')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        currency = request.POST.get('currency')
        message = request.POST.get('message')

        enquiry = EnquiryDetails.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, currency = currency, message = message)

        if enquiry:
            messages.success(request, 'Enquiry has been sent successfully.')
        else:
            messages.error(request, 'Enquiry Failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True) 

        return render(request, 'send-enquiry.html', context={ 'foreign_exchange': foreign_exchange, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
