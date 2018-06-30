from django.conf.urls import url
from foreign_exchange import views

urlpatterns = [
    url(r'^$', views.ForeignExchangePage.as_view(), name='foreignexchange'),
    url(r'^sendenquiry/(?P<status>[\w\-]+)/(?P<id>[0-9]+)/$', views.ForeignExchangeSendEnquiry.as_view(), name='sendenquiry'),
]