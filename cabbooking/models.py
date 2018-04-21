from django.db import models

# Create your models here.

class Cities(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='City Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        
