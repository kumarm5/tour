from django.conf.urls import url, include
from .views import FlightFixedDepartureChart, FlightFixedEnquiryDetails
from .api import SectorViewSet, SupplierDetailsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sector', SectorViewSet)
router.register(r'supplierdetails', SupplierDetailsViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', FlightFixedDepartureChart.as_view(template_name='flight_fixed_departure_chart.html'), name='fixed_departure_chart'),
    url(r'^(?P<id>[0-9]+)$', FlightFixedEnquiryDetails.as_view(template_name='flight_fixed_enquiry_details.html'), name='fixed_departure_details'),
]

urlpatterns = urlpatterns + router.urls