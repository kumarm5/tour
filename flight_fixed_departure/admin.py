from django.contrib import admin
from .models import *
from .forms import *
import logging
import pdb

# Register your models here.
    
class SectorAdmin(admin.ModelAdmin):
    form = SectorForm
    fields = (('sector_name', 'status'),)
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

class SupplierDetailsAdmin(admin.ModelAdmin):
    list_display = ('supplier_name','sectors','departure_date','return_date')
    form = SupplierDetailsForm
    fields = (('sectors', 'supplier_name', 'departure_time') , ('departure_flt_no', 'return_time', 'return_flt_no'), ('departure_date', 'return_date', 'total_departure_seats'), ('total_return_seats', 'departure_seat_availability', 'return_seat_availability'), ('dep_rate_flash', 'ret_rate_flash'), ('dep_rate_supplier', 'ret_rate_supplier'), ('other_details'))
    inlines = [SupplierPaymentInlineAdmin,]

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

class SupplierDepartureSeatInfoAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'first_name', 'last_name', 'sector_name', 'departure_date')
    form = SupplierDepartureSeatInfoForm   
    fields = (('supplier', 'first_name', 'middle_name') , ('last_name', 'mobile_no', 'date_of_birth'), ('passport_no', 'passport_exp', 'rate_given'), ('booking_agent',),)
    inlines = [SupplierDepartureSeatRemarkAdminInline,]

    def sector_name(self, obj):        
        return obj.supplier.sectors.sector_name
    sector_name.short_description = 'Sector'

    def departure_date(self, obj):
        return obj.supplier.departure_date
    departure_date.short_description = 'Departure Date'

    def save_model(self, request, obj, form, change):        
        if change is False:
            seat_avail = int(obj.supplier.departure_seat_availability) - 1
            SupplierDetails.objects.filter(pk=obj.supplier.pk).update(departure_seat_availability=seat_avail)

        super(SupplierDepartureSeatInfoAdmin, self).save_model(request, obj, form, change)

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

class SupplierReturnSeatInfoAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'first_name', 'last_name', 'sector_name', 'return_date')
    form = SupplierReturnSeatInfoForm
    fields = (('supplier', 'first_name', 'middle_name') , ('last_name', 'mobile_no', 'date_of_birth'), ('passport_no', 'passport_exp', 'rate_given'), ('booking_agent',),)
    inlines = [SupplierReturnSeatRemarkAdminInline,]
    
    def sector_name(self, obj):        
        return obj.supplier.sectors.sector_name
    sector_name.short_description = 'Sector'

    def return_date(self, obj):
        return obj.supplier.return_date
    return_date.short_description = 'Return Date'
            
admin.site.register(SupplierReturnSeatInfo, SupplierReturnSeatInfoAdmin)
