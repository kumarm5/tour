from django.contrib import admin
from django.contrib.admin.actions import delete_selected
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from .models import *
from .forms import *
from .export_mixin import ExportCsvMixin
import logging
import pdb
from django.core.mail import EmailMessage
# import httplib
import http.client
import re

# Register your models here.

@receiver(pre_delete, sender=SupplierReturnSeatInfo)
def return_seat_delete(sender, instance, **kwargs):    
    seat_avail = int(instance.supplier.return_seat_availability) + 1
    SupplierDetails.objects.filter(pk=instance.supplier.pk).update(return_seat_availability=seat_avail)	

@receiver(pre_delete, sender=SupplierDepartureSeatInfo)
def departure_seat_delete(sender, instance, **kwargs):
    seat_avail = int(instance.supplier.departure_seat_availability) + 1
    SupplierDetails.objects.filter(pk=instance.supplier.pk).update(departure_seat_availability=seat_avail)
        
# @receiver(post_delete)
# def comment_post_delete(sender, instance, *args, **kwargs):
#     pdb.set_trace()

@receiver(pre_delete, sender=OneWaySeat)
def oneway_seat_delete(sender, instance, **kwargs):
    seat_avail = int(instance.supplier.oneway_seat_availability) + 1
    SupplierDetails.objects.filter(pk=instance.supplier.pk).update(oneway_seat_availability=seat_avail)	

class SectorAdmin(admin.ModelAdmin):
    form = SectorForm
    fields = (('triptype', 'sector_name', 'status'),)
    list_display = ('sector_name', 'status')    
admin.site.register(Sector, SectorAdmin)

class SupplierPaymentInlineAdmin(admin.StackedInline):
    model = SupplierPaymentInline
    fk_name = 'supplier_details'
    fields = ('payment_remark',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return 0
        else:
            return 1

class SupplierDetailsAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('supplier_name','sectors','departure_date','return_date','oneway_date')
    form = SupplierDetailsForm
    fields = (('existing_supplier','triptype', 'sectors'), ('supplier_name'), ('departure_time', 'departure_flt_no', 'return_time'), ('return_flt_no', 'departure_date', 'return_date'), ('total_departure_seats', 'total_return_seats', 'departure_seat_availability'), ('return_seat_availability', 'dep_rate_flash', 'ret_rate_flash'), ('dep_rate_supplier', 'ret_rate_supplier'), ('oneway_date','oneway_rate_supplier', 'oneway_flt_no'), ('oneway_seat_availability','oneway_rate_flash', 'total_one_way_seats'), ('oneway_time'), ('other_details'))
    inlines = [SupplierPaymentInlineAdmin,]

    # def get_actions(self, request):
    #     actions = super(SupplierDetailsAdmin, self).get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
        
    # def mark_deleted(self, request, queryset):        
    #     print ("deleted")
    #     return delete_selected(self, request, queryset)

    # actions = [mark_deleted,]

    # actions = ['delete_selected']

    # def delete_selected(self, request, obj):
    #     for o in obj.all():
            # pdb.set_trace()
            # SupplierDetailsAdmin.objects.filter(invoice=o).update(billed=False)
            # o.delete()

    # delete_selected.short_description = 'Delete'
    actions = ["export_as_csv"]
admin.site.register(SupplierDetails, SupplierDetailsAdmin)

class SupplierDepartureSeatRemarkAdminInline(admin.StackedInline):
    model = SupplierDepartureSeatRemarkInline
    fk_name = 'supplier_seat'
    fields = ('seat_remark',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return 0
        else:
            return 1

class SupplierDepartureSeatInfoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('supplier', 'first_name', 'middle_name', 'last_name', 'sector_name', 'departure_date')
    form = SupplierDepartureSeatInfoForm   
    fields = (('supplier'), ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [SupplierDepartureSeatRemarkAdminInline,]

    def sector_name(self, obj):        
        return obj.supplier.sectors.sector_name
    sector_name.short_description = 'Sector'

    def departure_date(self, obj):
        return obj.supplier.departure_date.strftime('%d-%b-%Y')
    departure_date.short_description = 'Departure Date'

    def save_model(self, request, obj, form, change):
        if change is False:
            seat_avail = int(obj.supplier.departure_seat_availability) - 1
            SupplierDetails.objects.filter(pk=obj.supplier.pk).update(departure_seat_availability=seat_avail)

        super(SupplierDepartureSeatInfoAdmin, self).save_model(request, obj, form, change)

    actions = ["export_as_csv"]
admin.site.register(SupplierDepartureSeatInfo, SupplierDepartureSeatInfoAdmin)

class SupplierReturnSeatRemarkAdminInline(admin.StackedInline):
    model = SupplierReturnSeatRemarkInline
    fk_name = 'supplier_seat'
    fields = ('seat_remark',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return 0
        else:
            return 1

class SupplierReturnSeatInfoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('supplier', 'first_name', 'middle_name', 'last_name', 'sector_name', 'return_date')
    form = SupplierReturnSeatInfoForm
    fields = (('supplier') , ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [SupplierReturnSeatRemarkAdminInline,]
    
    def sector_name(self, obj):
        return obj.supplier.sectors.sector_name
    sector_name.short_description = 'Sector'

    def return_date(self, obj):
        return obj.supplier.return_date.strftime('%d-%b-%Y')
    return_date.short_description = 'Return Date'
        
    def save_model(self, request, obj, form, change):        
        if change is False:
            seat_avail = int(obj.supplier.return_seat_availability) - 1
            SupplierDetails.objects.filter(pk=obj.supplier.pk).update(return_seat_availability=seat_avail)

        super(SupplierReturnSeatInfoAdmin, self).save_model(request, obj, form, change)        
    
    actions = ["export_as_csv"]

admin.site.register(SupplierReturnSeatInfo, SupplierReturnSeatInfoAdmin)

class TripTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
admin.site.register(TripType, TripTypeAdmin)

class OneWaySeatRemarkInlineAdmin(admin.StackedInline):
    model = OneWaySeatRemarkInline
    fk_name = 'supplier_seat'
    fields = ('seat_remark',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return 0
        else:
            return 1

class OneWaySeatAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('supplier', 'first_name', 'middle_name', 'last_name', 'sector_name', 'one_way_date')
    form = OneWaySeatForm
    fields = (('supplier') , ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [OneWaySeatRemarkInlineAdmin,]

    def sector_name(self, obj):
        return obj.supplier.sectors.sector_name
    sector_name.short_description = 'Sector'

    def one_way_date(self, obj):
        return obj.supplier.oneway_date.strftime('%d-%b-%Y')
    one_way_date.short_description = 'One Way Date'

    def save_model(self, request, obj, form, change):
        if change is False:
            seat_avail = int(obj.supplier.oneway_seat_availability) - 1
            SupplierDetails.objects.filter(pk=obj.supplier.pk).update(oneway_seat_availability=seat_avail)

        super(OneWaySeatAdmin, self).save_model(request, obj, form, change)

    actions = ["export_as_csv"]

admin.site.register(OneWaySeat, OneWaySeatAdmin)

class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('terms', 'status')
    form = TermsAndConditionsForm
    fields = (('terms'), ('status'))

admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)

class EnquiryDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'sector', 'status', 'created_at')

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

            msg = EmailMessage(obj.sector, html_message, 'tanishtravels24@yahoo.co.in', [obj.email_id],['tanishtravels24@yahoo.co.in'])
            msg.content_subtype = "html"
            msg.send()

        super(EnquiryDetailsAdmin, self).save_model(request, obj, form, change)

admin.site.register(EnquiryDetails, EnquiryDetailsAdmin)    
