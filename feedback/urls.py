from django.conf.urls import url
from feedback import views

urlpatterns = [
    url(r'^$', views.FeedbackHome.as_view(), name='feedback'),
]