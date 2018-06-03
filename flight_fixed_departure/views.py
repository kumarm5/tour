from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sector, SupplierDetails, TermsAndConditions, EnquiryDetails
from tour_packages.models import Topics
from gallery.models import GalleryMenu
from django.contrib import messages
# Create your views here.

class FlightFixedDepartureChart(TemplateView):

    def get(self, request, *args):
        sector_details = Sector.objects.filter(status=True)
        supplier_details = SupplierDetails.objects.all()
        terms_and_conditions = TermsAndConditions.objects.filter(status = True)
        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        return render(request, self.template_name, {'sector_details': sector_details, 'supplier_details': supplier_details, 'terms_and_conditions': terms_and_conditions, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

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

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)
        return render(request, self.template_name, {'sector_id': int(sector_id), 'sector_details': sector_details, 'supplier_details': supplier_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus })

class FlightFixedEnquiryDetails(TemplateView):
    def get(self, request, *args, **kwargs):
        supplier_id = kwargs['id']

        try:
            supplier_details = SupplierDetails.objects.get(pk = supplier_id)
        except:
            supplier_details = None

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        return render(request, self.template_name, {'supplier_details': supplier_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus})
        
    def post(self, request, *args, **kwargs):
        supplier_id = kwargs['id']

        try:
            supplier_details = SupplierDetails.objects.get(pk = supplier_id)
        except:
            supplier_details = None

        mobile_num = request.POST.get('mobile_num')
        email_id = request.POST.get('email_id')
        username = request.POST.get('username')
        supplier = request.POST.get('supplier')
        message = request.POST.get('message')

        enquiry_details = EnquiryDetails.objects.create(mobile_num=mobile_num, email_id=email_id, username=username, supplier=supplier, message=message)

        if enquiry_details:
            messages.success(request, 'Enquiry has been sent successfully.')
        else:
            messages.error(request, 'Enquiry Failed.')

        tour_packages = Topics.objects.filter(status = True)
        gallery_menus = GalleryMenu.objects.filter(status = True)

        return render(request, self.template_name, {'supplier_details': supplier_details, 'tour_packages': tour_packages, 'gallery_menus': gallery_menus})