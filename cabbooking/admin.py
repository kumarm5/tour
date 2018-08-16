from django.contrib import admin
from .models import *
from .forms import *
from django.core.mail import EmailMessage
# import httplib
import http.client
import re

# Register your models here.

class CitiesAdmin(admin.ModelAdmin):
    form = CitiesForm
    list_display = ('title',)
    fields = (('title', 'image'),)
admin.site.register(Cities, CitiesAdmin)

class VehicleMasterAdmin(admin.ModelAdmin):
    form = VehicleMasterForm
    list_display = (('vehicle_name','category'))
    fields = (('vehicle_name','category'),)
admin.site.register(VehicleMaster, VehicleMasterAdmin)

class TermsAndConditionAdmin(admin.ModelAdmin):
    form = TermsAndConditionForm
    list_display = ('city',)
    fields = (('city'),('details'),)
admin.site.register(TermsAndCondition, TermsAndConditionAdmin)

admin.site.register(TariffDetails)

class TariffEnquiryAdmin(admin.ModelAdmin):
    list_display = ('username','status','created_at')

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

            html_message = obj.sms_or_email_message+'<br>'+html_message

            msg = EmailMessage(obj.subject, html_message, 'tanishtravels24@yahoo.co.in', [obj.email_id],['tanishtravels24@yahoo.co.in'])
            msg.content_subtype = "html"
            msg.send()

        super(TariffEnquiryAdmin, self).save_model(request, obj, form, change)

admin.site.register(TariffEnquiry, TariffEnquiryAdmin)

# admin.site.register(TariffEnquiry)

class CabRegisterAdmin(admin.ModelAdmin):
    list_display = ('agency_name','full_name','mobile_no','email_id','created_at')
admin.site.register(CabRegister, CabRegisterAdmin)

class RegisterVehicleAdmin(admin.ModelAdmin):
    list_display = ('type_vehicle','cab_no','agencyname', 'createddate')

    def agencyname(self, obj):
        return obj.cabregister

    def createddate(self, obj):
        return obj.cabregister.created_at

admin.site.register(RegisterVehicle, RegisterVehicleAdmin)

class ExtraPickUpDropAdmin(admin.ModelAdmin):
    # form = ExtraPickUpDropForm
    list_display = ('fromlocation', 'tolocation', 'vehiclename', 'action')
    fields = (('fromlocation', 'tolocation'),('vehiclename','vehicleprice'),('vehiclecategory','action'), ('vehicleimage'))
admin.site.register(ExtraPickUpDrop, ExtraPickUpDropAdmin)

class ExtraPickUpDropRequestAdmin(admin.ModelAdmin):
    list_display = ('route_vehicle', 'first_name', 'pick_up_date')
admin.site.register(ExtraPickUpDropRequest, ExtraPickUpDropRequestAdmin)

class ExtraPickUpDropTermsAdmin(admin.ModelAdmin):
    form = ExtraPickUpDropTermsForm
    list_display = ('title',)
    fields = (('title'),('details'),)
admin.site.register(ExtraPickUpDropTerms, ExtraPickUpDropTermsAdmin)

class PickUpDropLiveAdmin(admin.ModelAdmin):
    list_display = ('booking_type','first_name','last_name')    
admin.site.register(PickUpDropLive, PickUpDropLiveAdmin)

class PickUpDropLiveTermsAdmin(admin.ModelAdmin):
    form = PickUpDropLiveTermsForm
    list_display = ('title',)
    fields = (('title'),('details'),)
admin.site.register(PickUpDropLiveTerms, PickUpDropLiveTermsAdmin)

class TimeChangeAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(TimeChange, TimeChangeAdmin)

class PickDropLiveTripAdmin(admin.ModelAdmin):
    form = PickDropLiveTripForm
    list_display = ('title','status')
    fields = (('title', 'status'),)
admin.site.register(PickDropLiveTrip, PickDropLiveTripAdmin)
