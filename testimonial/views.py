from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Testimonial

# Create your views here.
class TestimonialPage(TemplateView):
    def get(self, request, *args, **kwargs):
        testimonials = Testimonial.objects.all()
        return render(request, 'testimonial.html', context={ 'testimonials': testimonials })