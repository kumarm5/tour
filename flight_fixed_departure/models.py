from django.db import models
# Create your models here.

class Sector(models.Model):    
    sector_name = models.CharField(max_length=150, unique=True, verbose_name="Sector")
    status = models.BooleanField(verbose_name="Status", default=True)
    
    def __str__(self):
        return self.sector_name

    class Meta:        
        db_table = 'sectors'
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'

class SupplierDetails(models.Model):
    supplier_name = models.CharField(max_length=150, verbose_name='Supplier Name')
    sectors = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='supplier_sector')
    departure_time = models.TimeField(blank=True, verbose_name='Departure Time')
    departure_flt_no = models.CharField(max_length=20, verbose_name='Dep. Flight No.')
    return_time = models.TimeField(blank=True, null=True, verbose_name='Return Time')
    return_flt_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Ret. Flight No.')
    departure_date = models.DateField(blank=True, verbose_name='Departure Date')
    return_date = models.DateField(blank=True, null=True, verbose_name='Return Date')
    departure_seat_availability = models.IntegerField(default=0, verbose_name='Departure Seat Availability')
    return_seat_availability = models.IntegerField(default=0, verbose_name='Return Seat Availability')
    total_departure_seats = models.IntegerField(default=0, verbose_name='Total Dep. Seats')
    total_return_seats = models.IntegerField(default=0, verbose_name='Total Ret. Seats')
    dep_rate_flash = models.IntegerField(default=0, verbose_name='Dep. Rate Flash')
    ret_rate_flash = models.IntegerField(default=0, verbose_name='Ret. Rate Flash')
    other_details = models.TextField(blank=True, null=True, verbose_name='Other Details')
    dep_rate_supplier = models.IntegerField(default=0)
    ret_rate_supplier = models.IntegerField(default=0)

    def __str__(self):
        return self.supplier_name

    class Meta:
        db_table = 'supplier_details'
        verbose_name = 'Supplier Detail'
        verbose_name_plural = 'Supplier Details'

class SupplierPaymentInline(models.Model):
    supplier_details = models.ForeignKey('SupplierDetails', on_delete=models.CASCADE, related_name='payment_remarks')
    payment_remark = models.TextField(blank=True, null=True, verbose_name='Payment Remarks')

    def __str__(self):
        return self.payment_remark

    class Meta:
        db_table = 'supplier_payment_remark'
        verbose_name = 'Supplier Payment Remark'
        verbose_name_plural = 'Supplier Payment Remarks'

class SupplierDepartureSeatInfo(models.Model):
    supplier = models.ForeignKey('SupplierDetails', on_delete=models.CASCADE, related_name='supplier_detail')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    mobile_no = models.IntegerField(default=0, blank=True, null=True, verbose_name='Mobile Number')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    passport_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='Passport Number')
    passport_exp = models.DateField(blank=True, null=True, verbose_name='Passport Expiry')
    booking_agent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Booking Agent')
    rate_given = models.IntegerField(default=0, verbose_name='Given Rate')

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'supplier_departure_seat_info'
        verbose_name = 'Passenger Departure Seat'
        verbose_name_plural = 'Passenger Departure Seats'


class SupplierDepartureSeatRemarkInline(models.Model):
    supplier_seat = models.ForeignKey('SupplierDepartureSeatInfo', on_delete=models.CASCADE, related_name='seat_supplier_departure_detail')
    seat_remark = models.TextField(blank=True, null=True, verbose_name='Remarks')

    def __str__(self):
        return self.seat_remark

    class Meta:
        db_table = 'seat_departure_remark'
        verbose_name = 'Seat Departure Remark'
        verbose_name_plural = 'Seat Departure Remarks'

class SupplierReturnSeatInfo(models.Model):
    supplier = models.ForeignKey('SupplierDetails', on_delete=models.CASCADE, related_name='supplier_details')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    mobile_no = models.IntegerField(default=0, blank=True, null=True, verbose_name='Mobile Number')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    passport_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='Passport Number')
    passport_exp = models.DateField(blank=True, null=True, verbose_name='Passport Expiry')
    booking_agent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Booking Agent')
    rate_given = models.IntegerField(default=0, verbose_name='Given Rate')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'supplier_return_seat_info'
        verbose_name = 'Passenger Return Seat'
        verbose_name_plural = 'Passenger Return Seats'

class SupplierReturnSeatRemarkInline(models.Model):
    supplier_seat = models.ForeignKey('SupplierReturnSeatInfo', on_delete=models.CASCADE, related_name='seat_supplier_return_detail')
    seat_remark = models.TextField(blank=True, null=True, verbose_name='Remarks')

    def __str__(self):
        return self.seat_remark

    class Meta:
        db_table = 'seat_return_remark'
        verbose_name = 'Seat Return Remark'
        verbose_name_plural = 'Seat Return Remarks'
