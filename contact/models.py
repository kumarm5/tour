from django.db import models
from django.utils.timezone import now
# Create your models here.

class PreferredSalesAgent(models.Model):
    company_name = models.CharField(max_length=300, verbose_name='Company Name')
    location = models.CharField(max_length=300, blank=True, null=True, verbose_name='Location')
    person_name = models.CharField(max_length=400, blank=True, null=True, verbose_name='Person Name')
    contact_number = models.CharField(max_length=500, blank=True, null=True, verbose_name='Contact')
    email_id = models.CharField(max_length=500, blank=True, null=True, verbose_name='Email Id')
    address = models.TextField(blank=True, null=True, verbose_name='Address')
    
    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Perferred Sales Agent'
        verbose_name_plural = 'Preferred Sales Agents'

class ContactInformation(models.Model):
    address = models.TextField(verbose_name='Address')
    banking = models.TextField(verbose_name='Banking')
    companies = models.TextField(verbose_name='Partner Group of Companies')

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Informations'

class ContactEnquiry(models.Model):
    mobile_num = models.CharField(max_length=20, null=True, blank=True, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email Id')
    username = models.CharField(max_length=200, verbose_name='Username')
    subject = models.CharField(max_length=400, null=True, blank=True, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    sms_or_email_message = models.TextField(null=True, blank=True, verbose_name='Email or SMS Message')
    send_sms = models.BooleanField(default=False, verbose_name='Send SMS')
    send_email = models.BooleanField(default=False, verbose_name='Send Email')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Contact Enquiry Detail'
        verbose_name_plural = 'Contact Enquiry Details'
