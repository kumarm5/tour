from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class ForeignExchangePage(TemplateView):
    def get(self, request, *args, **kwargs):
        foreign_exchanges = ForeignExchange.objects.filter(status=True)
        return render(request, 'foreign-exchange.html', context= { 'foreign_exchanges': foreign_exchanges })

class ForeignExchangeSendEnquiry(TemplateView):
    def get(self, request, *args, **kwargs):
        foreignexchange_id = int(kwargs['id'])
        try:
            foreign_exchange = ForeignExchange.objects.get(id = foreignexchange_id)
        except:
            foreign_exchange = None

        return render(request, 'send-enquiry.html', context={ 'foreign_exchange': foreign_exchange })