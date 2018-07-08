from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from django.contrib import messages
from .models import *
import http.client
# import httplib
from django.db.models import Q

# Create your views here.
class VisaTrack(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

    def post(self, request, *args, **kwargs):
        passport_num = request.POST.get('passport_num')
        country = request.POST.get('country')
        enquiry_date = request.POST.get('enquiry_date')

        passport_tracks = PassportTrack.objects.filter(passport_number = passport_num, added_date__gte = enquiry_date, country__icontains = country)

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'passport_tracks': passport_tracks })
        
class VisaLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        
        # if request.user.username:
        #     return redirect('Visa:visacountry') 

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-login.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
        
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        userpasswd = request.POST.get('userpasswd')
        formname = request.POST.get('formname')

        if formname == 'register':            
            dup_visa_profile = VisaProfile.objects.filter(mobile_num=phone)
            dup_user = User.objects.filter(email=email)

            if dup_visa_profile or dup_user:
                messages.error(request, 'Already registered')
            else:
                # code for sending sms
                conn = http.client.HTTPConnection("api.msg91.com")
                # conn = httplib.HTTPConnection("api.msg91.com")

                conn.request("GET", "/api/sendhttp.php?sender=TANISH&route=4&mobiles="+phone+"&authkey=91178Ahf3JuOcJ41W581c6f41&country=91&message=Your registration is complete to use our visa application")

                res = conn.getresponse()
                data = res.read()

                # print(data.decode("utf-8"))

                if data:
                    user = User.objects.create_user(username=email, email=email, password=userpasswd, first_name=first_name, last_name=last_name)
                    VisaProfile.objects.create(user=user, mobile_num=phone)

                    messages.success(request, 'Registeration successful.')

        elif formname == 'login':
            user = authenticate(username=email, password=userpasswd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("Visa:visacountry")
                else:
                    messages.error(request, 'You are not authorized to login.')
            else:
                messages.error(request, 'Login failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-login.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus })


class VisaCountries(TemplateView):    
    def get(self, request, *args, **kwargs):
        visacountries = VisaCountry.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, 'visa-country.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'visacountries': visacountries })

class VisaDetails(TemplateView):
    # def get_context_data(self, **kwargs):
    #     context = super(VisaDetails, self).get_context_data(**kwargs)
        
    def get(self, request, *args, **kwargs):
        try:
            visa_profile = VisaProfile.objects.get(user=request.user.pk)
        except:
            visa_profile = None

        country_id = kwargs['id']
        
        try:
            country = VisaCountry.objects.get(pk=country_id)
        except:
            country = None

        try:
            visa_info = VisaInfo.objects.get(pk=country_id)
        except:
            visa_info = None

        try:
            visa_downloads = VisaDownloads.objects.filter(visa_country=country_id)
        except:
            visa_downloads = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)        

        # maintaing the history when the user visit any details page of visa
        username = request.user
        email_id = request.user.email
        mobile_num = visa_profile.mobile_num
        activity = "Visited "+country.name+" Details Page"

        VisaHistory.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, activity = activity)

        return render(request, 'visa-details.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'country': country, 'visa_info': visa_info, 'visa_downloads': visa_downloads, 'country_id': country_id })

    def post(self, request, *args, **kwargs):
        
        download_text = request.POST.get('download_text')

        try:
            visa_profile = VisaProfile.objects.get(user=request.user.pk)
        except:
            visa_profile = None

        country_id = kwargs['id']
        
        try:
            country = VisaCountry.objects.get(pk=country_id)
        except:
            country = None

        try:
            visa_info = VisaInfo.objects.get(pk=country_id)
        except:
            visa_info = None

        try:
            visa_downloads = VisaDownloads.objects.filter(pk=country_id)
        except:
            visa_downloads = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)        

        # maintaing the history when the user visit any details page of visa
        username = request.user
        email_id = request.user.email
        mobile_num = visa_profile.mobile_num
        activity = download_text+" is downloaded"

        VisaHistory.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, activity = activity)

        return render(request, 'visa-details.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'country': country, 'visa_info': visa_info, 'visa_downloads': visa_downloads, 'country_id': country_id })

class Enquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        country_id = kwargs['id']

        try:
            country = VisaCountry.objects.get(pk=country_id)
        except:
            country = None

        try:
            visa_profile = VisaProfile.objects.get(user=request.user.pk)
        except:
            visa_profile = None

        return render(request, 'visa-enquiry.html', context={'country': country, 'visa_profile': visa_profile })

    def post(self, request, *args, **kwargs):
        country_id = kwargs['id']

        try:
            country = VisaCountry.objects.get(pk=country_id)
        except:
            country = None

        try:
            visa_profile = VisaProfile.objects.get(user=request.user.pk)
        except:
            visa_profile = None

        username = request.POST.get('username')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        visa_enquiry = VisaEnquiry.objects.create(username=username, mobile_num=mobile_num, email_id=email_id, subject=subject, message=message)

        if visa_enquiry:
            messages.success(request, "Your enquiry has been sent successfully")
        else:
            messages.error(request, "Enquiry Failure")

        return render(request, 'visa-enquiry.html', context={'country': country, 'visa_profile': visa_profile })
