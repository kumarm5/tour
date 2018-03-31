from django.conf.urls import url
from tour_packages import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)$', views.Tour.as_view(), name='tour'),
    url(r'^package/(?P<id>[0-9]+)$', views.Packages.as_view(), name='package'),
    url(r'^packagedetails/(?P<id>[0-9]+)$', views.PackageInfo.as_view(), name='packagedetails'),
]
