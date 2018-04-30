from django.conf.urls import url
from .views import ServicePage, SendEnquiry

urlpatterns = [
    url(r'^$', ServicePage.as_view(), name='services'),
    url(r'^service-enquiry/(?P<id>[0-9]+)$', SendEnquiry.as_view(), name='service-enquiry'),
]
