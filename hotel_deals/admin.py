from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_display = ('name',)
    fields = (('name', 'images'),)
admin.site.register(City, CityAdmin)

class HotelAdmin(admin.ModelAdmin):
    form = HotelForm
    list_display = ('city', 'name')
    fields = (('city',), ('name','hotel_images'), ('description'),)
admin.site.register(Hotel, HotelAdmin)

class HotelImagesAdmin(admin.ModelAdmin):
    form = HotelImagesForm
    list_display = ('hotel','title')
    fields = (('hotel',), ('title','hotel_images'))
admin.site.register(HotelImages, HotelImagesAdmin)


class HotelDetailsAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'title')
    form = HotelDetailsForm
    fields = (('hotel', 'hotel_images'), ('title'), ('overview'), ('inclusion'), ('exclusion'), ('how_to_book'), ('hotel_info'), ('map_image'))

admin.site.register(HotelDetails, HotelDetailsAdmin)
