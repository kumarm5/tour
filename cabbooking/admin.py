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
