from django.db import models
from django.utils.timezone import now
# Create your models here.

class TripType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    status = models.BooleanField(verbose_name='Status', default=True)

    def __str__(self):
        return self.name

class Sector(models.Model):
    sector_name = models.CharField(max_length=150, unique=True, verbose_name="Sector")    
    triptype = models.ForeignKey('TripType', on_delete=models.DO_NOTHING, verbose_name='Type of Trip')
    status = models.BooleanField(verbose_name="Status", default=True)
    
    def __str__(self):
        return self.sector_name

    class Meta:        
        db_table = 'sectors'
        verbose_name = '     Sector'
        verbose_name_plural = '     Sectors'

class SupplierDetails(models.Model):
    supplier_name = models.CharField(max_length=150, verbose_name='Supplier Name')
    triptype = models.ForeignKey('TripType', on_delete=models.DO_NOTHING, verbose_name='Type of Trip')
    sectors = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='supplier_sector')
    departure_time = models.TimeField(blank=True, null=True, verbose_name='Departure Time')
    departure_flt_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Dep. Flight No.')
    return_time = models.TimeField(blank=True, null=True, verbose_name='Return Time')
    return_flt_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Ret. Flight No.')
    departure_date = models.DateField(blank=True, null=True, verbose_name='Departure Date')
    return_date = models.DateField(blank=True, null=True, verbose_name='Return Date')
    departure_seat_availability = models.IntegerField(blank=True, null=True, verbose_name='Departure Seat Availability')
    return_seat_availability = models.IntegerField(blank=True, null=True, verbose_name='Return Seat Availability')
    total_departure_seats = models.IntegerField(blank=True, null=True, verbose_name='Total Dep. Seats')
    total_return_seats = models.IntegerField(blank=True, null=True, verbose_name='Total Ret. Seats')
    dep_rate_flash = models.IntegerField(blank=True, null=True, verbose_name='Dep. Rate Flash')
    ret_rate_flash = models.IntegerField(blank=True, null=True, verbose_name='Ret. Rate Flash')
    other_details = models.TextField(blank=True, null=True, verbose_name='Other Details')
    dep_rate_supplier = models.IntegerField(blank=True, null=True)
    ret_rate_supplier = models.IntegerField(blank=True, null=True)
    oneway_time = models.TimeField(blank=True, null=True, verbose_name='One Way Time')
    oneway_date = models.DateField(blank=True, null=True, verbose_name='One Way Date')
    oneway_rate_supplier = models.IntegerField(blank=True, null=True, verbose_name='One Way Rate Supplier')
    oneway_seat_availability = models.IntegerField(blank=True, null=True, verbose_name='One Way Seat Availability')
    oneway_rate_flash = models.IntegerField(blank=True, null=True, verbose_name='One Way Rate Flash')
    oneway_flt_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='One Way Flight No.')
    total_one_way_seats = models.IntegerField(blank=True, null=True, verbose_name='Total One Way Seats')

    def __str__(self):
        return self.supplier_name

    class Meta:
        db_table = 'supplier_details'
        verbose_name = '    Supplier Detail'
        verbose_name_plural = '    Supplier Details'

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
    # sector = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='departure_seat_sector')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    mobile_no = models.CharField(max_length=30, blank=True, null=True, verbose_name='Mobile Number')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    passport_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='Passport Number')
    passport_exp = models.DateField(blank=True, null=True, verbose_name='Passport Expiry')
    booking_agent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Booking Agent')
    rate_given = models.IntegerField(default=0, verbose_name='Given Rate')

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'supplier_departure_seat_info'
        verbose_name = '   Round Trip Departure Seat'
        verbose_name_plural = '   Round Trip Departure Seats'

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
    # sector = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='return_seat_sector')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    mobile_no = models.CharField(max_length=30, blank=True, null=True, verbose_name='Mobile Number')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    passport_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='Passport Number')
    passport_exp = models.DateField(blank=True, null=True, verbose_name='Passport Expiry')
    booking_agent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Booking Agent')
    rate_given = models.IntegerField(default=0, verbose_name='Given Rate')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'supplier_return_seat_info'
        verbose_name = '  Round Trip Return Seat'
        verbose_name_plural = '  Round Trip Return Seats'

class SupplierReturnSeatRemarkInline(models.Model):
    supplier_seat = models.ForeignKey('SupplierReturnSeatInfo', on_delete=models.CASCADE, related_name='seat_supplier_return_detail')
    seat_remark = models.TextField(blank=True, null=True, verbose_name='Remarks')

    def __str__(self):
        return self.seat_remark

    class Meta:
        db_table = 'seat_return_remark'
        verbose_name = 'Seat Return Remark'
        verbose_name_plural = 'Seat Return Remarks'

class OneWaySeat(models.Model):
    supplier = models.ForeignKey('SupplierDetails', on_delete=models.CASCADE, related_name='oneway_supplierdetails')
    # sector = models.ForeignKey('Sector', on_delete=models.CASCADE, related_name='oneway_seat_sector')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Last Name')
    mobile_no = models.CharField(max_length=30, blank=True, null=True, verbose_name='Mobile Number')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    passport_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='Passport Number')
    passport_exp = models.DateField(blank=True, null=True, verbose_name='Passport Expiry')
    booking_agent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Booking Agent')
    rate_given = models.IntegerField(default=0, blank=True, null=True, verbose_name='Given Rate')

    # @property
    # def supplier_details(self):
    #     return self.supplier.supplier_name+'-'+supplier.sectors.sector_name

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'one_way_seat'
        verbose_name = '   One Way Seat'
        verbose_name_plural = '   One Way Seats'

class OneWaySeatRemarkInline(models.Model):
    supplier_seat = models.ForeignKey('OneWaySeat', on_delete=models.CASCADE, related_name='oneway_seat_detail')
    seat_remark = models.TextField(blank=True, null=True, verbose_name='Remarks')

    def __str__(self):
        return self.seat_remark

    class Meta:
        db_table = 'oneway_seat_remark'
        verbose_name = 'One Way Seat Remark'
        verbose_name_plural = 'One Way Seat Remarks'

class TermsAndConditions(models.Model):
    terms = models.CharField(max_length=700, verbose_name='Terms And Conditions')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.terms

    class Meta:
        db_table = 'terms_and_conditions'
        verbose_name = 'Term and Condition'
        verbose_name_plural = 'Terms and Conditions'
        

class EnquiryDetails(models.Model):
    STATUS_CHOICES = (
        ("GENERATED", "GENERATED"),
        ("IN-PROCESS", "IN-PROCESS"),
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
    )

    mobile_num = models.CharField(max_length=20, null=True, blank=True, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email Id')
    username = models.CharField(max_length=200, verbose_name='Username')
    sector = models.CharField(max_length=200, null=True, blank=True, verbose_name='sector')
    message = models.TextField(verbose_name='Message')
    sms_or_email_message = models.TextField(null=True, blank=True, verbose_name='Email or SMS Message')
    send_sms = models.BooleanField(default=False, verbose_name='Send SMS')
    send_email = models.BooleanField(default=False, verbose_name='Send Email')
    created_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="GENERATED")
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Enquiry Detail'
        verbose_name_plural = 'Enquiry Details'
