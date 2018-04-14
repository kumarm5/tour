from django.conf.urls import url
from .views import VisaTrack, VisaLogin

urlpatterns = [
    url(r'track/$', VisaTrack.as_view(), name='visatrack'),
    url(r'visalogin/$', VisaLogin.as_view(), name='visalogin'),
]
