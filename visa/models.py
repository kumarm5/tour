from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    added_date = models.DateTimeField(verbose_name='Date Time')
    country = models.CharField(blank=True, null=True, max_length=500, verbose_name='Country')
    
    def __str__(self):
        return self.passport_number

    class Meta:
        verbose_name = 'Passport Tracking'
        verbose_name_plural = 'Passport Trackings'

class VisaProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number', unique=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Visa User Profile'
        verbose_name_plural = 'Visa User Profiles'

class VisaCountry(models.Model):
    name = models.CharField(max_length=300, verbose_name='Name')
    image = models.FileField(upload_to='documents/', verbose_name='Image')
    details = models.CharField(max_length=500, verbose_name='Details')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class VisaInfo(models.Model):
    visa_country = models.ForeignKey(VisaCountry, on_delete=models.CASCADE)
    visa_details = models.TextField(verbose_name='visa details')

    def __str__(self):
        return self.visa_country.name

    class Meta:
        verbose_name = 'Visa Detail'
        verbose_name_plural = 'Visa Details'

class VisaDownloads(models.Model):
    visa_country = models.ForeignKey(VisaCountry, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='Files')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'

class VisaEnquiry(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=100, verbose_name='Email Address')
    subject = models.CharField(max_length=500, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

class VisaHistory(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=100, verbose_name='Email Address')
    activity = models.CharField(max_length=500, verbose_name='Activity')
    created_at = models.DateTimeField(default=now, verbose_name='Created At')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
        