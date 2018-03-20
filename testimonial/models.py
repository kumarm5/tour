from django.db import models

# Create your models here.

class Testimonial(models.Model):
    first_name = models.CharField(max_length=60, verbose_name='First Name')
    last_name = models.CharField(blank=True, null=True, max_length=60, verbose_name='Last Name')
    address = models.CharField(blank=True, null=True, max_length=800, verbose_name='Address')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    images = models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Images')
    rating = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

