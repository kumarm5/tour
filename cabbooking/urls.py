from django.conf.urls import include, url
from .views import CabRentalCities

urlpatterns = [
    url(r'^cities/', CabRentalCities.as_view(), name='cabrentalcities'),
]