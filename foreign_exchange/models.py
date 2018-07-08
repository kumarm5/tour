from django.db import models

# Create your models here.
class ForeignExchange(models.Model):
    currency_name = models.CharField(max_length=500, verbose_name='Currency Name')
    buy = models.CharField(max_length=300, verbose_name='Buy')
    sale = models.CharField(max_length=300, verbose_name='Sale')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = 'Foreign Exchange'
        verbose_name_plural = 'Foreign Exchanges'

class EnquiryDetails(models.Model):
    STATUS_CHOICES = (
        ("IN-PROGRESS", "IN-PROGRESS"),
        ("COMPLETED", "COMPLETED"),
    )

    mobile_num = models.CharField(max_length=20, null=True, blank=True, verbose_name='Mobile Number')
    email_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email Id')
    username = models.CharField(max_length=200, verbose_name='Username')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="IN-PROGRESS")
    currency = models.CharField(max_length=200, null=True, blank=True, verbose_name='currency')
    sms_or_email_message = models.TextField(null=True, blank=True, verbose_name='Email or SMS Message')
    send_sms = models.BooleanField(default=False, verbose_name='Send SMS')
    send_email = models.BooleanField(default=False, verbose_name='Send Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Enquiry Detail'
        verbose_name_plural = 'Enquiry Details'

class TermsAndCondition(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    details = models.TextField(verbose_name='Details')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Terms and Condition'
        verbose_name_plural = 'Terms and Conditions'
