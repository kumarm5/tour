from django.conf.urls import url
from hotel_deals import views

urlpatterns = [
    url(r'^$', views.Cities.as_view(), name='cities'),
    url(r'^hotel/(?P<id>[0-9]+)$', views.Hotels.as_view(), name='hotel'),
    url(r'^hoteldetails/(?P<id>[0-9]+)$', views.HotelInfo.as_view(), name='hoteldetails'),
]
