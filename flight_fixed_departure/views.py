from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sector, SupplierDetails
import pdb
# Create your views here.

class FlightFixedDepartureChart(TemplateView):

    def get(self, request, *args):
        
        sector_details = Sector.objects.filter(status=True)

        supplier_details = SupplierDetails.objects.all()

        return render(request, self.template_name, {'sector_details': sector_details, 'supplier_details': supplier_details})

    def post(self, request, *args):
        
        sector_id = request.POST['sector_id'];

        sector_details = Sector.objects.filter(status=True)

        if sector_id == '0':
            supplier_details = SupplierDetails.objects.all()
        else:
            try:
                supplier_details = SupplierDetails.objects.filter(sectors = sector_id)
            except:
                supplier_details = None

        return render(request, self.template_name, {'sector_id': int(sector_id), 'sector_details': sector_details, 'supplier_details': supplier_details})
