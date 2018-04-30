from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='Image')
    description = models.TextField(verbose_name='Description')
    url = models.CharField(max_length=500, verbose_name='Link')
    url_text = models.CharField(max_length=500, verbose_name='Link Text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service Detail'
        verbose_name_plural = 'Service Details'

class ServiceSendEnquiry(models.Model):
    mobile_number = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_address = models.CharField(max_length=100, verbose_name='Email Id')
    username = models.CharField(max_length=150, verbose_name='Username')
    subject = models.CharField(max_length=200, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Send Enquiry'
        verbose_name_plural = 'Send Enquiries'

