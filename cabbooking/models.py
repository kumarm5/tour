from django.db import models

# Create your models here.

class Cities(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='City Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        

class VehicleMaster(models.Model):
    vehicle_name = models.CharField(max_length=300, verbose_name='Vehicle Name')
    category = models.CharField(max_length=300, verbose_name='Category')

    def __str__(self):
        return self.vehicle_name

    class Meta:
        verbose_name = ' Vehicle'
        verbose_name_plural = ' Vehicles'

class TermsAndCondition(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='CityTerms')
    details = models.TextField(verbose_name='Details')

    def __str__(self):
        return self.city.title

    class Meta:
        verbose_name = 'Terms and Condition'
        verbose_name_plural = 'Terms and Conditions'

class TariffDetails(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='CityTariff', verbose_name='City')
    vehicle_master = models.ForeignKey(VehicleMaster, on_delete=models.CASCADE, related_name='TariffVehicle', verbose_name='Vehicle')
    four_hour = models.CharField(max_length=10, verbose_name='04 HRS')
    eight_hour = models.CharField(max_length=10, verbose_name='08 HRS')
    twelve_hour = models.CharField(max_length=10, verbose_name='12 HRS')
    extra_per_km = models.CharField(max_length=10, verbose_name='Extra Per KM')
    extra_per_hour = models.CharField(max_length=10, verbose_name='Extra Per Hour')
    outstation_per_km = models.CharField(max_length=10, verbose_name='Outstation Per KM')
    outstation_per_hour = models.CharField(max_length=10, verbose_name='Outstation Per Hour')

    def __str__(self):
        return self.city.title

    class Meta:
        verbose_name = 'Tariff Detail'
        verbose_name_plural = 'Tariff Details'


class TariffEnquiry(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=100, verbose_name='Email Address')
    subject = models.CharField(max_length=500, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Tariff Enquiry'
        verbose_name_plural = 'Tariff Enquiries'