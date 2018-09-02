from django.db import models
from django.utils.timezone import now

# Create your models here.
class Topics(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Topic')
    status = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = '  Topic'
        verbose_name_plural = '  Topics'

class Tours(models.Model):
    tour_topic = models.ForeignKey('Topics', on_delete=models.CASCADE, verbose_name='Tour Topic')
    title = models.CharField(max_length=250, verbose_name='Title')
    tour_images = models.FileField(upload_to='documents/', verbose_name='Tour Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '  Tour'
        verbose_name_plural = '  Tours'

class TourPackages(models.Model):
    tour = models.ForeignKey('Tours', on_delete=models.CASCADE, verbose_name='Tours')
    title = models.CharField(max_length=450, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    package_images = models.FileField(upload_to='documents/', verbose_name='Package Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Package'
        verbose_name_plural = ' Packages'

class PackageImages(models.Model):
    package = models.ForeignKey('TourPackages', on_delete=models.CASCADE, verbose_name='Package')    
    title = models.CharField(max_length=450, verbose_name='Title')
    package_images = models.FileField(upload_to='documents/', verbose_name='Package Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Package Image'
        verbose_name_plural = 'Package Images'

class PackageDetails(models.Model):
    package = models.ForeignKey('TourPackages', on_delete=models.CASCADE, verbose_name='Package')
    title = models.CharField(max_length=400, blank=True, null=True, verbose_name='Title')
    overview = models.TextField(blank=True, null=True, verbose_name='Overview')
    inclusion = models.TextField(blank=True, null=True, verbose_name='Inclusion')
    exclusion = models.TextField(blank=True, null=True, verbose_name='Exclusion')
    how_to_book = models.TextField(blank=True, null=True, verbose_name='How to book')
    tour_info = models.TextField(blank=True, null=True, verbose_name='Tour Info')
    map_image = models.FileField(upload_to='documents/', verbose_name='Map Image')
    package_images = models.ManyToManyField(PackageImages, verbose_name='Package Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Package Details'
        verbose_name_plural = 'Package Details'

class TourPackageEnquiry(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=100, verbose_name='Email Address')
    subject = models.CharField(max_length=500, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    sms_or_email_message = models.TextField(null=True, blank=True, verbose_name='Email or SMS Message')
    send_sms = models.BooleanField(default=False, verbose_name='Send SMS')
    send_email = models.BooleanField(default=False, verbose_name='Send Email')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
