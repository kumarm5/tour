from django.conf.urls import url
from passport import views

urlpatterns = [
    url(r'^$', views.PassportView.as_view(), name='home'),    
]
