from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedback
from django.contrib import messages

# Create your views here.

class FeedbackHome(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'feedback.html', context={})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        rating = request.POST.get('rating')
        messages.success(request, 'Thank you for your feedback.')
        feedback = Feedback.objects.create(name=username, mobile_number=mobile, message=message, rating=rating)
        return render(request, 'feedback.html', context={})