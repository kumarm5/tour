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


class About(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    about_text = models.TextField(verbose_name='Text')
    first_image = models.ImageField(upload_to = 'documents/', null=True, blank=True)
    second_image = models.ImageField(upload_to = 'documents/', null=True, blank=True)
    first_image_name = models.CharField(max_length=100, verbose_name='First image name', null=True, blank=True)
    second_image_name = models.CharField(max_length=100, verbose_name='Second image name', null=True, blank=True)
    first_image_position = models.CharField(max_length=100, verbose_name='First image position', null=True, blank=True)
    second_image_position = models.CharField(max_length=100, verbose_name='Second image position', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
