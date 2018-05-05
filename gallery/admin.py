from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class GalleryMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    form = GalleryMenuForm
    fields = (('title','status'),)

admin.site.register(GalleryMenu, GalleryMenuAdmin)

class GallerySubCatAdmin(admin.ModelAdmin):
    list_display = ('gallery_topic', 'title')
    form = GallerySubCatForm
    fields = (('gallery_topic'), ('title', 'sub_category_images'))

admin.site.register(GallerySubCat, GallerySubCatAdmin)


class GallerySubCatImageAdmin(admin.ModelAdmin):
    list_display = ('sub_category', 'title')
    form = GallerySubCatImageForm
    fields = (('sub_category'), ('title', 'images'))

admin.site.register(GalleryImages, GallerySubCatImageAdmin)


admin.site.register(GalleryVideos)
