from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from news.models import NewsInfo
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
# import httplib
import http.client
import re

# Create your views here.
class Contact(TemplateView):
    def get(self, request, **kwargs):
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        contact_information = ContactInformation.objects.last()
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'contact_information': contact_information, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, **kwargs):
        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        username = request.POST.get('username')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_enquiry = ContactEnquiry.objects.create(mobile_num=mobile_num, email_id=email_id, username=username, subject=subject, message=message)

        if contact_enquiry:
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

            html_message = 'Mobile Number: '+mobile_num+'<br>'+'Email Address: '+email_id+'<br>'+'Username: '+username+'<br>'+'Subject: '+subject+'<br>'+'Message: '+message+'<br>'+html_message

            msg = EmailMessage(subject, html_message, 'tanishtravels24@yahoo.co.in', [],['tanishtravels24@yahoo.co.in'])
            msg.content_subtype = "html"
            msg.send()

            messages.success(request, 'Your Message has been sent successfully.')
        else:
            messages.error(request, 'Your Message has not been sent.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        contact_information = ContactInformation.objects.last()
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        return render(request, 'contact.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'contact_information': contact_information, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class PreferredSalesAgentInfo(TemplateView):
    def get(self, request, *args, **kwargs):
        preferredsalesagents = PreferredSalesAgent.objects.all()
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]
        return render(request, 'preferred-sales-agent.html', context={ 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'preferredsalesagents': preferredsalesagents, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
