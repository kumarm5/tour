from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'address')
    form = TestimonialForm
    fields = (('first_name', 'last_name'), ('images', 'rating'), ('address'), ('description') )

admin.site.register(Testimonial, TestimonialAdmin)