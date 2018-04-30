from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from django.contrib import messages
from .models import *

# Create your views here.

class ServicePage(TemplateView):
    def get(self, request, *args, **kwargs):
        service_details = Services.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'services.html', context={ 'service_details': service_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

class SendEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        service_id = int(kwargs['id'])
        try:
            service = Services.objects.get(id = service_id)
        except:
            service = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'service-send-enquiry.html', context={ 'service': service, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

    def post(self, request, *args, **kwargs):
        mobile_number = request.POST.get('mobile_number')
        email_address = request.POST.get('email_address')
        username = request.POST.get('username')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        enquiry = ServiceSendEnquiry.objects.create(mobile_number=mobile_number, email_address=email_address, username=username, subject=subject, message=message)

        if enquiry:
            messages.success(request,'Message has been sent successfully.')
        else:
            messages.error(request,'Message sending failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'service-send-enquiry.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })