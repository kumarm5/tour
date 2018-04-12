from django.conf.urls import url
from .views import PreferredSalesAgentInfo, Contact

urlpatterns = [    
    url(r'^$', Contact.as_view(), name='contact'),
    url(r'^preferredsalesagent/$', PreferredSalesAgentInfo.as_view(), name='preferredsalesagent'),
]
