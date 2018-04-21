from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class PassportTrackTypeAdmin(admin.ModelAdmin):
    form = PassportTrackTypeForm
    list_display = ('track_type','status')
    fields = (('track_type','status'),)
admin.site.register(PassportTrackType, PassportTrackTypeAdmin)

class PassportTrackAdmin(admin.ModelAdmin):
    form = PassportTrackForm
    list_display = ('passport_number', 'track_type', 'added_date')
    fields = (('passport_number', 'track_type'),('additional_details'))    
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
    fields = (('visa_country'), ('visa_details'))
admin.site.register(VisaInfo, VisaInfoAdmin)

class VisaDownloadsAdmin(admin.ModelAdmin):
    form = VisaDownloadsForm
    list_display = ('title', 'image')
    fields = (('visa_country'),('title','image'))
admin.site.register(VisaDownloads, VisaDownloadsAdmin)

class VisaEnquiryAdmin(admin.ModelAdmin):
    form = VisaEnquiryForm
    list_display = ('username', 'mobile_num', 'email_id')
    fields = (('username','mobile_num'), ('email_id','subject'), ('message'))
admin.site.register(VisaEnquiry, VisaEnquiryAdmin)

class VisaHistoryAdmin(admin.ModelAdmin):
    form = VisaHistoryForm
    list_display = ('username', 'mobile_num', 'email_id')
    fields = (('username','mobile_num','email_id'),('activity'))
admin.site.register(VisaHistory, VisaHistoryAdmin)
