from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    fields = (('title'), ('description'), ('status'))
    list_display = ('title', 'status')
admin.site.register(NewsInfo, NewsAdmin)

