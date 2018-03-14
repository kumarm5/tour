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
