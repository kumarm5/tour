from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.
class ForeignExchangeAdmin(admin.ModelAdmin):
    list_display = ('currency_name', 'buy', 'sale')
    form = ForeignExchangeForm
    fields = (('currency_name', 'buy'), ('sale', 'status'))
admin.site.register(ForeignExchange, ForeignExchangeAdmin)