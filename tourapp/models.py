from django.db import models

# Create your models here.

class HomeImageSlider(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='Image')
    description = models.TextField(verbose_name='Description')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Image Slider'
        verbose_name_plural = 'Image Sliders'

