from django.conf.urls import url, include
from .views import News

urlpatterns = [
    url(r'^$', News.as_view(template_name='news.html'), name='news'),
]
