from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'status')
    form = TopicForm
    fields = (('topic', 'status'),)

admin.site.register(Topics, TopicAdmin)


class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_topic', 'title')
    form = TourForm
    fields = (('title'), ('tour_images', 'tour_topic'),)

admin.site.register(Tours, TourAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('tour', 'title')
    form = PackageForm
    fields = (('tour'), ('title', 'package_images'),('description'))

admin.site.register(TourPackages, PackageAdmin)


class PackageImagesAdmin(admin.ModelAdmin):
    list_display = ('package', 'package_images')
    form = PackageImagesForm
    fields = (('package'), ('title','package_images'), )

admin.site.register(PackageImages, PackageImagesAdmin)


class PackageDetailsAdmin(admin.ModelAdmin):
    list_display = ('package', 'title')
    form = PackageDetailsForm
    fields = (('package', 'package_images'), ('title'), ('overview'), ('inclusion'), ('exclusion'), ('how_to_book'), ('tour_info'), ('map_image'))

admin.site.register(PackageDetails, PackageDetailsAdmin)
