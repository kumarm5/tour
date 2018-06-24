from django.conf.urls import include, url
from .views import CabRentalCities, Tariff, TariffDetailEnquiry, CabRegisteration, PickDropLive, ExtraPickDrop, get_vehicles, get_from_location, get_to_location, get_extra_vehicle

urlpatterns = [
    url(r'^cities/', CabRentalCities.as_view(), name='cabrentalcities'),
    url(r'^tariff/(?P<id>[0-9]+)$', Tariff.as_view(), name='tariff'),
    url(r'^tariff-enquiry/(?P<id>[0-9]+)$', TariffDetailEnquiry.as_view(), name='tariffenquiry'),
    url(r'^cab-registeration/', CabRegisteration.as_view(), name='cabregisteration'),
    url(r'^pick-drop-live/', PickDropLive.as_view(), name='pickdroplive'),
    url(r'^extra-pick-drop/', ExtraPickDrop.as_view(), name='extrapickdrop'),
    url(r'^get-vehicles', get_vehicles, name='getvehicles'),
    url(r'^fromlocation', get_from_location, name='fromlocation'),
    url(r'^tolocation', get_to_location, name='tolocation'),
    url(r'^extravehicle', get_extra_vehicle, name='extravehicle')
]