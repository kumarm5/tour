from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from .models import *
from news.models import NewsInfo
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import *
import http.client
# import httplib

# Create your views here.
class Tour(TemplateView):
    def get(self, request, **kwargs):
        tour_topic_id = int(kwargs['id'])
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_details = Tours.objects.filter(tour_topic_id = tour_topic_id)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'tour.html', context={ 'tour_packages': tour_packages, 'tour_details': tour_details, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class Packages(TemplateView):
    def get(self, request, **kwargs):
        tour_id = int(kwargs['id'])        
        tour_package_details = TourPackages.objects.filter(tour = tour_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'package.html', context={ 'tour_packages': tour_packages, 'tour_package_details': tour_package_details, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class PackageInfo(TemplateView):
    def get(self, request, **kwargs):
        package_id = int(kwargs['id'])
        package_details = PackageDetails.objects.get(pk = package_id)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        return render(request, 'package-details.html', context= { 'package_details': package_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class Enquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        package_id = kwargs['id']
        try:
            package_details = PackageDetails.objects.get(pk = package_id)
        except:
            package_details = None
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        return render(request, 'tour-enquiry.html', context={'package_details': package_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        package_id = kwargs['id']
        try:
            package_details = PackageDetails.objects.get(pk = package_id)
        except:
            package_details = None

        username = request.POST.get('username')
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        tour_enquiry = TourPackageEnquiry.objects.create(username=username, mobile_num=mobile_num, email_id=email_id, subject=subject, message=message)

        if tour_enquiry:
            html_message = '\
                <br>\
                <p>Regards and Thanks,</p>\
                <p>Jai D Solanki&nbsp;<strong>(Managing&nbsp;Partner)</strong></p>\
                <p><strong>Tanish Travel Hut</strong></p>\
                <p><strong>HO :</strong>&nbsp;Sr No: 33, Ceratec City, Ph-2, No: 702 ,</p>\
                <p>D wing , Katraj Kondhwa Road,</p>\
                <p>Tilekar Nagar, Yewalewadi, Pune -411048.</p>\
                <p>Email:&nbsp;<a href="mailto:tanishtravels24@yahoo.co.in" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88159" rel="nofollow" target="_blank">tanishtravels24@yahoo.co.in</a></p>\
                <p>Only&nbsp;For Acc.Use:&nbsp;<a href="mailto:accounts.tanishtravels@yahoo.com" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88156" rel="nofollow" target="_blank">accounts.tanishtravels@yahoo.com</a></p>\
                <p>Register yourself&nbsp;&amp; get exciting rates on our Online Travel Portal:&nbsp;<a href="http://tthboutique.com/" rel="nofollow" target="_blank">http://tthboutique.com</a>&nbsp;</p>\
                <p>Website:&nbsp;<a href="http://www.tanishtravelhut.com/" target="_blank">www.tanishtravelhut.com</a></p>\
                <p>Contact&nbsp; :09890176353, 09420177963.</p>\
                <p><strong>FLIGHTS</strong>&nbsp;|<strong>&nbsp;</strong><strong>HOLIDAYS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>CAR RENTALS</strong><strong>&nbsp;</strong><strong>|</strong><strong>&nbsp;VISAS&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>BUS</strong><strong>&nbsp;|</strong>&nbsp;<strong>HOTELS</strong><strong>&nbsp;</strong><strong>|</strong>&nbsp;<strong>TRAVEL INSURANCE&nbsp;</strong><strong>|</strong><strong>&nbsp;</strong><strong>FOREX&nbsp;</strong><strong>| INT&#39;L SIM CARD</strong></p>\
                <p><strong>Download our Mobile App from play store type. Tanish Travel hut</strong></p>\
                <p><strong>Like our Face book page:&nbsp;<a href="https://www.facebook.com/tanishtravelhutpune/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_87994" rel="nofollow" target="_blank">https://www.facebook.com/tanishtravelhutpune/</a></strong></p>\
                <p>Linked&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.linkedin.com/in/tanishtravelhutpune/" target="_blank">www.linkedin.com/in/tanishtravelhutpune/</a>&nbsp;</p>\
                <p><strong>Twitter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :&nbsp;<a href="http://twitter.com/tanishtravelhut" target="_blank">twitter.com/tanishtravelhut</a></strong></p>\
                <p><strong>Instagram&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;:&nbsp;<a href="http://www.instagram.com/jaisolanki24/" id="m_-648102519220567386yiv6790210145yui_3_16_0_ym19_1_1503551224247_88335" rel="nofollow" target="_blank">www.instagram.com/tanishtravelhutpune/</a></strong></p>\
                <p><strong>Skype&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;<a href="http://www.instagram.com/jaisolanki24/" rel="nofollow" target="_blank">jaisolanki2012/</a></strong></p>\
                <p><strong>Save No. In your Mobile:&nbsp;09890176353&nbsp;to get latest offers &amp; Updates.</strong></p>\
                <p><strong>-------------------------------------------------------------------------------&nbsp;</strong></p>\
                <p><strong>Tanish Group:</strong></p>\
                <p><strong>TANISH PROPERTY HUT &amp; CONSULTANT PVT LTD / SHWETA&#39;S FOOD / EXPLORA TOURISM</strong><strong>&nbsp;</strong><strong>/ TULSI COLLECTION /</strong></p>\
                <p><strong>JAI &nbsp;ENTERPRISES</strong><strong>/ OPTION FITNESS EQUIPMENT&#39;S</strong></p>\
                <p><strong>P</strong>&nbsp;Please take care of the environment, print only if necessary.</p>\
                <p><em>Note: This email message is for the sole use of the intended recipient(s) and may contain CONFIDENTIAL and PRIVILEGED information. Any unauthorized review; use, disclosure or distribution is prohibited.&nbsp; If you are not the intended recipient, please contact the sender by reply email and destroy all copies of the original message and any attachments. The recipient should check this email and any attachments for the presence of viruses. Tanish&nbsp;Travel Hut&nbsp;accepts no liability for any damage caused by any virus transmitted by this email.</em></p>'

            html_message = 'User Name is '+username+'<br>Mobile Number is '+mobile_num+'<br>Email Id is '+email_id+'<br>Subject is '+subject+'<br>Message is '+message+'<br>'+html_message

            email_message = EmailMessage(subject, html_message, 'tanishtravels24@yahoo.co.in', [],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, "Your enquiry has been sent successfully")
        else:
            messages.error(request, "Enquiry Failure")

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:3]
        gallery_menus = GalleryMenu.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)

        return render(request, 'tour-enquiry.html', context={'package_details': package_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
