from django.conf.urls import include, url
from .views import CabRentalCities, Tariff, TariffDetailEnquiry, CabRegisteration, get_vehicles

urlpatterns = [
    url(r'^cities/', CabRentalCities.as_view(), name='cabrentalcities'),
    url(r'^tariff/(?P<id>[0-9]+)$', Tariff.as_view(), name='tariff'),
    url(r'^tariff-enquiry/(?P<id>[0-9]+)$', TariffDetailEnquiry.as_view(), name='tariffenquiry'),
    url(r'^cab-registeration', CabRegisteration.as_view(), name='cabregisteration'),
    url(r'^get-vehicles', get_vehicles, name='getvehicles')
]