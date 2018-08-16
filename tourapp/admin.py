from django.contrib import admin
from .forms import *
from .models import *
# Register your models here.

class HomeImageSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    form = HomeImageSliderForm
    fields = (('title','image','status'),('description'),)

admin.site.register(HomeImageSlider, HomeImageSliderAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    form = AboutForm
    fields = (('title','status'), ('about_text'))

admin.site.register(About, AboutAdmin)