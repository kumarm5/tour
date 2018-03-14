from django.db import models

# Create your models here.
class Topics(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Topic')
    status = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

class Tours(models.Model):
    tour_topic = models.ForeignKey('Topics', on_delete=models.CASCADE, verbose_name='Tour Topic')
    title = models.CharField(max_length=250, verbose_name='Title')
    tour_images = models.FileField(upload_to='documents/', verbose_name='Tour Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'        