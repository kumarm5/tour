from django.shortcuts import render
from django.views.generic import TemplateView
from tour_packages.models import Topics
from gallery.models import GalleryMenu, GalleryImages
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from news.models import NewsInfo

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

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'foreign-exchange.html', context= { 'foreign_exchanges': foreign_exchanges, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'term_and_cond': term_and_cond, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

class ForeignExchangeSendEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        foreignexchange_id = int(kwargs['id'])
        status = kwargs['status']

        try:
            foreign_exchange = ForeignExchange.objects.get(id = foreignexchange_id)
        except:
            foreign_exchange = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'send-enquiry.html', context={ 'foreign_exchange': foreign_exchange, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'status': status, 'footer_news': footer_news, 'footer_galleries': footer_galleries })

    def post(self, request, *args, **kwargs):
        foreignexchange_id = int(kwargs['id'])
        status = kwargs['status']

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

            html_message = 'User Name is '+username+'<br>Mobile Number is '+mobile_num+'<br>Email Id is '+email_id+'<br>Currency is '+currency+'<br>Message is '+message+'<br>'+html_message

            email_message = EmailMessage(currency, html_message, 'tanishtravels24@yahoo.co.in', [email_id],['tanishtravels24@yahoo.co.in'])
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, 'Enquiry has been sent successfully.')
        else:
            messages.error(request, 'Enquiry Failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True) 

        footer_galleries = GalleryImages.objects.all()[:4]
        footer_news = NewsInfo.objects.all()[:2]

        return render(request, 'send-enquiry.html', context={ 'foreign_exchange': foreign_exchange, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus, 'status': status, 'footer_news': footer_news, 'footer_galleries': footer_galleries })
