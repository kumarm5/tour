from django.conf.urls import url
from tour_packages import views

urlpatterns = [    
    url(r'^(?P<id>[0-9]+)$', views.Tour.as_view(), name='tour'),
]
