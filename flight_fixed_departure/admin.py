from django.contrib import admin
from django.contrib.admin.actions import delete_selected
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from .models import *
from .forms import *
from .export_mixin import ExportCsvMixin
import logging
import pdb

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
    fields = (('triptype', 'sectors'), ('supplier_name'), ('departure_time', 'departure_flt_no', 'return_time'), ('return_flt_no', 'departure_date', 'return_date'), ('total_departure_seats', 'total_return_seats', 'departure_seat_availability'), ('return_seat_availability', 'dep_rate_flash', 'ret_rate_flash'), ('dep_rate_supplier', 'ret_rate_supplier'), ('oneway_date','oneway_rate_supplier', 'oneway_flt_no'), ('oneway_seat_availability','oneway_rate_flash', 'total_one_way_seats'), ('oneway_time'), ('other_details'))
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
    fields = (('supplier', 'sector'), ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [SupplierDepartureSeatRemarkAdminInline,]

    def sector_name(self, obj):        
        return obj.sector.sector_name
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
    fields = (('supplier', 'sector') , ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [SupplierReturnSeatRemarkAdminInline,]
    
    def sector_name(self, obj):        
        return obj.sector.sector_name
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

# class TripTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status')
# admin.site.register(TripType, TripTypeAdmin)

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
    fields = (('supplier', 'sector') , ('first_name', 'middle_name', 'last_name'), ('mobile_no', 'date_of_birth', 'passport_no'), ('passport_exp', 'rate_given', 'booking_agent',),)
    inlines = [OneWaySeatRemarkInlineAdmin,]

    def sector_name(self, obj):
        return obj.sector.sector_name
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

