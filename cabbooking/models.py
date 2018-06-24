from django.db import models

# Create your models here.

class Cities(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    image = models.FileField(upload_to='documents/', verbose_name='City Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '   City'
        verbose_name_plural = '   Cities'
        

class VehicleMaster(models.Model):
    vehicle_name = models.CharField(max_length=300, verbose_name='Vehicle Name')
    category = models.CharField(max_length=300, verbose_name='Category')

    def __str__(self):
        return self.vehicle_name

    class Meta:
        verbose_name = '  Vehicle'
        verbose_name_plural = '  Vehicles'

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
    four_hour = models.CharField(max_length=10, verbose_name='4 Hrs/40 Kms')
    eight_hour = models.CharField(max_length=10, verbose_name='8 Hrs/80 Kms')
    ten_hour = models.CharField(max_length=10, default='0', verbose_name='10 Hrs/100 Kms')
    twelve_hour = models.CharField(max_length=10, verbose_name='12 Hrs/120 Kms')
    extra_per_km = models.CharField(max_length=10, verbose_name='Extra Per KM')
    extra_per_hour = models.CharField(max_length=10, verbose_name='Extra Per Hour')
    outstation_per_km = models.CharField(max_length=10, verbose_name='Outstation Per KM')
    outstation_per_hour = models.CharField(max_length=10, verbose_name='Outstation Per Day')

    def __str__(self):
        return self.city.title

    class Meta:
        verbose_name = ' Tariff Detail'
        verbose_name_plural = ' Tariff Details'


class TariffEnquiry(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    mobile_num = models.CharField(max_length=15, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=100, verbose_name='Email Address')
    subject = models.CharField(max_length=500, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ' Tariff Enquiry'
        verbose_name_plural = ' Tariff Enquiries'

class CabRegister(models.Model):
    agency_name = models.CharField(max_length=200, verbose_name='Agency Name')
    full_name = models.CharField(max_length=200, verbose_name='Full Name')
    mobile_no = models.CharField(max_length=200, verbose_name='Mobile No')
    email_id = models.CharField(max_length=200, verbose_name='Email Id')
    bank_name = models.CharField(max_length=200, verbose_name='Bank Name')
    account_no = models.CharField(max_length=200, verbose_name='Account No')
    name_in_account = models.CharField(max_length=200, verbose_name='Account Name')
    ifsc_code = models.CharField(max_length=200, verbose_name='IFSC Code')
    branch = models.CharField(max_length=200, verbose_name='Branch')
    address = models.TextField(verbose_name='Address')
    
    def __str__(self):
        return self.agency_name

    class Meta:
        verbose_name = 'Cab Registeration'
        verbose_name_plural = 'Cab Registerations'

class RegisterVehicle(models.Model):
    cabregister = models.ForeignKey(CabRegister, on_delete=models.DO_NOTHING)
    type_vehicle = models.CharField(max_length=200, verbose_name='Vehicle Type')
    purchase_date = models.CharField(max_length=200, verbose_name='Purchase Date')
    cab_no = models.CharField(max_length=200, verbose_name='Cab Number')
    image = models.FileField(upload_to='documents/', null=True, blank=True, verbose_name='Vehicle Image')

    def __str__(self):
        return self.type_vehicle

    class Meta:
        verbose_name = 'Registered Vehicle'
        verbose_name_plural = 'Registered Vehicles'

class ExtraPickUpDrop(models.Model):
    routename = models.CharField(max_length=200, verbose_name='Route Name')
    fromlocation = models.CharField(max_length=200, verbose_name='From Location')
    tolocation = models.CharField(max_length=200, verbose_name='To Location')
    vehiclename = models.CharField(max_length=200, verbose_name='Vehicle Name')    
    vehicleimage = models.FileField(upload_to='documents/', verbose_name='Vehicle Image')
    vehiclecategory = models.CharField(max_length=200, verbose_name='Vehicle Category')
    vehicleprice = models.CharField(max_length=200, verbose_name='Vehicle Price')
    status = models.BooleanField(verbose_name="Status", default=True)

    def __str__(self):
        return self.routename

    class Meta:
        verbose_name = 'Extra Pick Up Drop'
        verbose_name_plural = 'Extra Pick Up Drops'

class ExtraPickUpDropRequest(models.Model):
    route_vehicle = models.ForeignKey(ExtraPickUpDrop, on_delete=models.DO_NOTHING)
    mobile_num = models.CharField(max_length=200, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=200, verbose_name='Email Id')
    first_name = models.CharField(max_length=200, verbose_name='First Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    pick_up_date = models.CharField(max_length=200, verbose_name='Pick Up Date')
    pick_up_time = models.CharField(max_length=200, verbose_name='Pick Up Time')
    message = models.TextField(null=True, blank=True, verbose_name='Message')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Extra Pick Up Drop Request'
        verbose_name_plural = 'Extra Pick Up Drop Requests'

