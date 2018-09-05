from django.contrib import admin
from .models import *
from .forms import *
from .export_mixin import ExportCsvMixin
from django.core.mail import EmailMessage
# import httplib
import http.client
import re

# Register your models here.

class PassportTrackTypeAdmin(admin.ModelAdmin):
    form = PassportTrackTypeForm
    list_display = ('track_type','status')
    fields = (('track_type','status'),)
admin.site.register(PassportTrackType, PassportTrackTypeAdmin)

class PassportTrackAdmin(admin.ModelAdmin, ExportCsvMixin):
    form = PassportTrackForm
    list_display = ('passport_number', 'track_type', 'country', 'added_date', 'additional_details')
    fields = (('passport_number', 'track_type'), ('country', 'added_date'),('additional_details'))  
    actions = ["export_as_csv"]  
admin.site.register(PassportTrack, PassportTrackAdmin)

class VisaProfileAdmin(admin.ModelAdmin):
    form = VisaProfileForm
    list_display = ('user', 'mobile_num')
    fields = (('user'),('mobile_num'),)
admin.site.register(VisaProfile, VisaProfileAdmin)

class VisaCountryAdmin(admin.ModelAdmin):
    form = VisaCountryForm
    list_display = ('name','details')
    fields = (('name','image'),('details'))
admin.site.register(VisaCountry, VisaCountryAdmin)

class VisaInfoAdmin(admin.ModelAdmin):
    form = VisaInfoForm
    list_display = ('visa_country',)
    fields = (('visa_country'), ('visa_details'), ('message'))
admin.site.register(VisaInfo, VisaInfoAdmin)

class VisaDownloadsAdmin(admin.ModelAdmin):
    form = VisaDownloadsForm
    list_display = ('title', 'image')
    fields = (('visa_country'),('title','image'))
admin.site.register(VisaDownloads, VisaDownloadsAdmin)

class VisaEnquiryAdmin(admin.ModelAdmin):
    form = VisaEnquiryForm
    list_display = ('username', 'mobile_num', 'email_id','status','created_at')
    fields = (('username','mobile_num'), ('email_id','subject'), ('message'),('sms_or_email_message'),('send_sms')
    ,('send_email'),('created_at'),('status'))

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

        super(VisaEnquiryAdmin, self).save_model(request, obj, form, change)

admin.site.register(VisaEnquiry, VisaEnquiryAdmin)

class VisaHistoryAdmin(admin.ModelAdmin):
    form = VisaHistoryForm
    list_display = ('username', 'mobile_num', 'email_id', 'activity', 'created_at')
    fields = (('username','mobile_num','email_id'),('activity'))
admin.site.register(VisaHistory, VisaHistoryAdmin)
