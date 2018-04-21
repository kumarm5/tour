"""tourproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', logout, {'next_page': '/admin/login/'}),
    url(r'^', include('tourapp.urls')),
    url(r'^departurechart/', include('flight_fixed_departure.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^tour/', include('tour_packages.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^testimonials/', include('testimonial.urls')),
    url(r'^foreignexchange/', include('foreign_exchange.urls')),
    url(r'^hoteldeals/', include('hotel_deals.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^visa/', include('visa.urls', namespace="Visa")),
    url(r'^cabbooking/', include('cabbooking.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administration'