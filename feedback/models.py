from django.db import models
from django.utils.timezone import now

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    mobile_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number')
    message = models.TextField(blank=True, null=True, verbose_name='Description')
    rating = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    remark = models.TextField(blank=True, null=True, verbose_name='Remark')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
