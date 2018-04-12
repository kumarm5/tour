from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class PassportTrackTypeAdmin(admin.ModelAdmin):
    form = PassportTrackTypeForm
    list_display = ('track_type','status')
    fields = ('track_type','status')
admin.site.register(PassportTrackType, PassportTrackTypeAdmin)

class PassportTrackAdmin(admin.ModelAdmin):
    list_display = ('passport_number', 'track_type', 'added_date')
admin.site.register(PassportTrack, PassportTrackAdmin)
