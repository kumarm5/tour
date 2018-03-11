from django.db import models

# Create your models here.

class NewsInfo(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    status = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News Information'
        verbose_name_plural = 'News Informations'
