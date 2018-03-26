from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('images', 'updated_at')
    forms = InsuranceForm
    fields = (('images'), )

admin.site.register(Insurance, InsuranceAdmin)