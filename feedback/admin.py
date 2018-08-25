from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    form = FeedbackForm
    list_display = ('name','mobile_number','created_at')
    fields = (('name','mobile_number','rating'),('message'),('remark'))
admin.site.register(Feedback, FeedbackAdmin)
