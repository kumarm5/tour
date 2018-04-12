from django.conf.urls import url
from tourapp import views

urlpatterns = [    
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^contact/$', views.Contact.as_view(), name='contact'),
]
