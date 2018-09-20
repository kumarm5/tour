from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView, View
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo
from django.contrib import messages
from .models import *
import http.client
# import httplib
from django.db.models import Q
from django.core.mail import EmailMessage

# Create your views here.
class VisaTrack(TemplateView):
    def get(self, request, *args, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        passport_num = request.POST.get('passport_num')
        country = request.POST.get('country')
        enquiry_date = request.POST.get('enquiry_date')

        passport_tracks = PassportTrack.objects.filter(passport_number = passport_num, added_date__gte = enquiry_date, country__icontains = country).order_by('added_date')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-tracking.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'passport_tracks': passport_tracks, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
        
class VisaLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        
        # if request.user.username:
        #     return redirect('Visa:visacountry') 

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-login.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
        
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

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-login.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })


class VisaCountries(TemplateView):    
    def get(self, request, *args, **kwargs):
        visacountries = VisaCountry.objects.order_by('name')
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-country.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'visacountries': visacountries, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class VisaDetails(TemplateView):
    # def get_context_data(self, **kwargs):
    #     context = super(VisaDetails, self).get_context_data(**kwargs)
        
    def get(self, request, *args, **kwargs):
        try:
            visa_profile = VisaProfile.objects.get(user=request.user)
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

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'visa-details.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'country': country, 'visa_info': visa_info, 'visa_downloads': visa_downloads, 'country_id': country_id, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):

        try:
            visa_profile = VisaProfile.objects.get(user=request.user)
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

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        form_name = ''
        form_name = request.POST.get('form_name')
        if form_name == 'mail_form':
            
            email_id = request.POST.get('email_id')
            username = request.POST.get('username')

            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>TTH- Team</p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong><strong>|</strong><strong>&nbsp;</strong><strong>PASSPORT ASSISTANCE</strong></p>       <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p>Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            html_message = visa_info.visa_details+'<br>'+html_message

            email_message = EmailMessage('Visa Info for '+visa_info.visa_country.name, html_message, 'tanishtravels24@yahoo.co.in', [email_id],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()
        else:
            download_text = request.POST.get('download_text')

            # maintaing the history when the user visit any details page of visa
            username = request.user
            email_id = request.user.email
            mobile_num = visa_profile.mobile_num
            activity = download_text+" is downloaded"

            VisaHistory.objects.create(username = username, mobile_num = mobile_num, email_id = email_id, activity = activity)

        return render(request, 'visa-details.html', context={'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'country': country, 'visa_info': visa_info, 'visa_downloads': visa_downloads, 'country_id': country_id, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

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

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)

        return render(request, 'visa-enquiry.html', context={'country': country, 'visa_profile': visa_profile, 'footer_news': footer_news, 'footer_galleries': footer_galleries, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus  })

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
            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>TTH- Team</p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong><strong>|</strong><strong>&nbsp;</strong><strong>PASSPORT ASSISTANCE</strong></p>       <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p>Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            html_message = 'User Name is '+username+'<br>Mobile Number is '+mobile_num+'<br>Email Id is '+email_id+'<br>Subject is '+subject+'<br>Message is '+message+'<br>'+html_message

            email_message = EmailMessage(subject, html_message, 'tanishtravels24@yahoo.co.in', [],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, "Your enquiry has been sent successfully")
        else:
            messages.error(request, "Enquiry Failure")

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)

        return render(request, 'visa-enquiry.html', context={'country': country, 'visa_profile': visa_profile, 'footer_news': footer_news, 'footer_galleries': footer_galleries, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })
