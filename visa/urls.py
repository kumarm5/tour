from django.conf.urls import url
from .views import VisaTrack

urlpatterns = [
    url(r'track/$', VisaTrack.as_view(), name='visatrack'),
]
