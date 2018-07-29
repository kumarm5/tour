from django.contrib import admin
from .models import *

# Register your models here.
class PassportInfoAdmin(admin.ModelAdmin):
    list_display = ('given_name','status','created_at')
admin.site.register(PassportInfo, PassportInfoAdmin)

# admin.site.register(PassportInfo)