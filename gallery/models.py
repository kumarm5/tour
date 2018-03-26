from django.db import models

# Create your models here.
class GalleryMenu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Topic')
    status = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery Menu'
        verbose_name_plural = 'Gallery Menu'

class GallerySubCat(models.Model):
    gallery_topic = models.ForeignKey('GalleryMenu', on_delete=models.CASCADE, verbose_name='Gallery Topic')
    title = models.CharField(max_length=100, verbose_name='Title')
    sub_category_images = models.FileField(upload_to='documents/', verbose_name='Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Category'

class GalleryImages(models.Model):
    sub_category = models.ForeignKey('GallerySubCat', on_delete=models.CASCADE, verbose_name='Sub Category')
    title = models.CharField(max_length=300, verbose_name='Title')
    images = models.FileField(upload_to='documents/', verbose_name='Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub Category Images'
        verbose_name_plural = 'Sub Category Images'