from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sector, SupplierDetails
# Create your views here.

class FlightFixedDepartureChart(TemplateView):

    def get(self, request, *args):
        
        sector_details = Sector.objects.filter(status=True)

        supplier_details = SupplierDetails.objects.all()

        return render(request, self.template_name, {'sector_details': sector_details, 'supplier_details': supplier_details})
