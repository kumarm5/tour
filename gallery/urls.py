from django.conf.urls import url
from gallery import views

urlpatterns = [    
    url(r'^gallery/(?P<id>[0-9]+)$', views.Gallery.as_view(template_name='gallery.html'), name='gallery'), 
    url(r'^category/(?P<id>[0-9]+)$', views.GallerySubCatImage.as_view(template_name='gallery_category.html'), name='category'),
]
