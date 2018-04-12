from django.db import models

# Create your models here.
class PassportTrackType(models.Model):
    track_type = models.CharField(max_length=500, verbose_name='Track Type')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.track_type

    class Meta:
        verbose_name = 'Tracking Type'
        verbose_name_plural = 'Tracking Types'

class PassportTrack(models.Model):
    passport_number = models.CharField(max_length=500, verbose_name='Passport Number')
    track_type = models.ForeignKey('PassportTrackType', on_delete=models.CASCADE, verbose_name='Track Type')
    additional_details = models.TextField(blank=True, null=True, verbose_name='Additional Details')
    added_date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return self.passport_number

    class Meta:
        verbose_name = 'Passport Tracking'
        verbose_name_plural = 'Passport Trackings'
