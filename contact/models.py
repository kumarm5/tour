from django.db import models

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
