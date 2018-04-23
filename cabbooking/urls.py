from django.conf.urls import include, url
from .views import CabRentalCities, Tariff, TariffDetailEnquiry

urlpatterns = [
    url(r'^cities/', CabRentalCities.as_view(), name='cabrentalcities'),
    url(r'^tariff/(?P<id>[0-9]+)$', Tariff.as_view(), name='tariff'),
    url(r'^tariff-enquiry/(?P<id>[0-9]+)$', TariffDetailEnquiry.as_view(), name='tariffenquiry'),
]