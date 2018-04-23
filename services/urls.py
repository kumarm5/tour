from django.conf.urls import url
from .views import ServicePage

urlpatterns = [
    url(r'^$', ServicePage.as_view(), name='services'),
]