from django.db import models

# Create your models here.
class Insurance(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    images = models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='PDF')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'