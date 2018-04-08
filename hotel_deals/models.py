from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=250, verbose_name='City')
    images = models.FileField(upload_to='documents/', verbose_name='City Images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '  City'
        verbose_name_plural = '  Cities'

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Cities')
    name = models.CharField(max_length=300, verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    hotel_images = models.FileField(upload_to='documents/', verbose_name='Hotel Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Hotel'
        verbose_name_plural = ' Hotels'
        
class HotelImages(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, verbose_name='Hotel')
    title = models.CharField(max_length=450, verbose_name='Title')
    hotel_images = models.FileField(upload_to='documents/', verbose_name='Hotel Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hotel Image'
        verbose_name_plural = 'Hotel Images'

class HotelDetails(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, verbose_name='Hotel')
    title = models.CharField(max_length=400, blank=True, null=True, verbose_name='Title')
    overview = models.TextField(blank=True, null=True, verbose_name='Overview')
    inclusion = models.TextField(blank=True, null=True, verbose_name='Inclusion')
    exclusion = models.TextField(blank=True, null=True, verbose_name='Exclusion')
    how_to_book = models.TextField(blank=True, null=True, verbose_name='How to book')
    hotel_info = models.TextField(blank=True, null=True, verbose_name='Hotel Info')
    map_image = models.FileField(upload_to='documents/', verbose_name='Map Image')
    hotel_images = models.ManyToManyField(HotelImages, verbose_name='Hotel Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hotel Details'
        verbose_name_plural = 'Hotel Details'
        
