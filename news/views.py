from django.shortcuts import render
from django.views.generic import TemplateView
from .models import NewsInfo

# Create your views here.
class News(TemplateView):
    def get(self, request, *args):
        news_details = NewsInfo.objects.filter(status=True)        
        return render(request, self.template_name, {'news_details': news_details})
