from django.conf.urls import url
from testimonial import views

urlpatterns=[
    url(r'^$', views.TestimonialPage.as_view(), name='testimonial'),
]