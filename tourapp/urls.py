from django.conf.urls import url
from tourapp import views

urlpatterns = [    
    url(r'^$', views.HomeView.as_view(), name='home'),
]
