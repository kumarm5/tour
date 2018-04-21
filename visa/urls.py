from django.conf.urls import url
from .views import VisaTrack, VisaLogin, VisaCountries, VisaDetails, Enquiry
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'track/$', VisaTrack.as_view(), name='visatrack'),
    url(r'visalogin/$', VisaLogin.as_view(), name='visalogin'),
    url(r'country/$', login_required(VisaCountries.as_view(), login_url='visalogin'), name='visacountry'),
    url(r'visadetails/(?P<id>[0-9]+)$', login_required(VisaDetails.as_view(), login_url='visalogin'), name='visadetails'),
    url(r'enquiry/(?P<id>[0-9]+)$', login_required(Enquiry.as_view()), name='visaenquiry'),
]
