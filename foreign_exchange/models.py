from django.db import models

# Create your models here.
class ForeignExchange(models.Model):
    currency_name = models.CharField(max_length=500, verbose_name='Currency Name')
    buy = models.CharField(max_length=300, verbose_name='Buy')
    sale = models.CharField(max_length=300, verbose_name='Sale')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    status = models.BooleanField(default=True, verbose_name='Status')