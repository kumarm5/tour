from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from django.contrib import messages
from .models import *

# Create your views here.

class CabRentalCities(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        cities = Cities.objects.all()
        return render(request, 'cab-rental-cities.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'cities': cities })

class Tariff(TemplateView):
    def get(self, request, *args, **kwargs):
        city_id = kwargs['id']

        try:
            city_detail = Cities.objects.get(pk=city_id)
        except:
            city_detail = None

        try:
            term_and_cond = TermsAndCondition.objects.get(city = city_id)
        except:
            term_and_cond = None
            
        tariff_details = TariffDetails.objects.filter(pk=city_id)
        
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        return render(request, 'car-tariff.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'city_detail': city_detail, 'tariff_details': tariff_details })

class TariffDetailEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        tariff_id = kwargs['id']

        try:
            tariff_detail = TariffDetails.objects.get(pk=tariff_id)
        except:
            tariff_detail = None

        return render(request, 'tariff-enquiry.html', context={ 'tariff_detail': tariff_detail })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        tariff_enquiry = TariffEnquiry.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, subject = subject, message = message)

        if tariff_enquiry:
            messages.success(request, 'Enquiry has been sent successfully.')
        else:
            messages.error(request, 'Enquiry Failed.')

        tariff_id = kwargs['id']

        try:
            tariff_detail = TariffDetails.objects.get(pk=tariff_id)
        except:
            tariff_detail = None

        return render(request, 'tariff-enquiry.html', context={ 'tariff_detail': tariff_detail })

