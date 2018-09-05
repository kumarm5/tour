from django.contrib import admin
from .models import *
from .forms import *
from django.core.mail import EmailMessage
# import httplib
import http.client
import re

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'status')
    form = TopicForm
    fields = (('topic', 'status'),)

admin.site.register(Topics, TopicAdmin)


class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_topic', 'title')
    form = TourForm
    fields = (('title'), ('tour_images', 'tour_topic'),)

admin.site.register(Tours, TourAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('tour', 'title')
    form = PackageForm
    fields = (('tour'), ('title', 'package_images'),('description'))

admin.site.register(TourPackages, PackageAdmin)


class PackageImagesAdmin(admin.ModelAdmin):
    list_display = ('package', 'package_images')
    form = PackageImagesForm
    fields = (('package'), ('title','package_images'), )

admin.site.register(PackageImages, PackageImagesAdmin)


class PackageDetailsAdmin(admin.ModelAdmin):
    list_display = ('package', 'title')
    form = PackageDetailsForm
    fields = (('package', 'package_images'), ('title'), ('overview'), ('inclusion'), ('exclusion'), ('how_to_book'), ('tour_info'), ('map_image'))

admin.site.register(PackageDetails, PackageDetailsAdmin)

class TourPackageEnquiryAdmin(admin.ModelAdmin):    
    list_display = ('username', 'mobile_num', 'email_id','created_at')
    fields = (('username','mobile_num'), ('email_id','subject'), ('message'),('sms_or_email_message'),('send_sms')
    ,('send_email'),('created_at'))

    def save_model(self, request, obj, form, change):
        if obj.send_sms:
            TAG_RE = re.compile(r'<[^>]+>')
            sms_or_email_message = TAG_RE.sub('', obj.sms_or_email_message)
            conn = http.client.HTTPConnection("api.msg91.com")
            # conn = httplib.HTTPConnection("api.msg91.com")
            conn.request("GET", "/api/sendhttp.php?sender=TANISH&route=4&mobiles="+obj.mobile_num+"&authkey=91178Ahf3JuOcJ41W581c6f41&country=91&message="+sms_or_email_message+"")
            res = conn.getresponse()
            data = res.read()

        if obj.send_email:
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

            html_message = obj.sms_or_email_message+'<br>'+html_message

            msg = EmailMessage(obj.subject, html_message, 'tanishtravels24@yahoo.co.in', [obj.email_id],['tanishtravels24@yahoo.co.in'])
            msg.content_subtype = "html"
            msg.send()

        super(TourPackageEnquiryAdmin, self).save_model(request, obj, form, change)

admin.site.register(TourPackageEnquiry, TourPackageEnquiryAdmin)
