from django.contrib import admin
from .models import *
from .forms import *

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

admin.site.register(TariffEnquiry)

class CabRegisterAdmin(admin.ModelAdmin):
    list_display = ('agency_name','full_name','mobile_no','email_id')
admin.site.register(CabRegister, CabRegisterAdmin)

class RegisterVehicleAdmin(admin.ModelAdmin):
    list_display = ('type_vehicle','cab_no')
admin.site.register(RegisterVehicle, RegisterVehicleAdmin)

class ExtraPickUpDropAdmin(admin.ModelAdmin):
    form = ExtraPickUpDropForm
    list_display = ('fromlocation', 'tolocation', 'vehiclename', 'status')
    fields = (('routename','fromlocation', 'tolocation'),('vehiclename','vehicleprice','vehiclecategory'), ('vehicleimage','status'))
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
