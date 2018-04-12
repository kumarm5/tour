from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class PreferredSalesAgentAdmin(admin.ModelAdmin):
    form = PreferredSalesAgentForm
    list_display = ('company_name', 'location')
    fields = (('company_name', 'location', 'person_name'),('email_id','contact_number'),('address',))
admin.site.register(PreferredSalesAgent, PreferredSalesAgentAdmin)

