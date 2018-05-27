from django.db import models

# Create your models here.


class SupplierImages(models.Model):
    supplier = models.ForeignKey('SupplierDirectory', on_delete=models.DO_NOTHING, verbose_name='Supplier')    
    title = models.CharField(max_length=450, verbose_name='Title')
    supplier_images = models.FileField(upload_to='documents/', verbose_name='Supplier Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Supplier Image'
        verbose_name_plural = 'Supplier Images'


class SupplierDirectory(models.Model):
    country = models.CharField(max_length=300, null=True, blank=True, verbose_name='Country')
    product = models.CharField(max_length=300, null=True, blank=True, verbose_name='Product')
    company_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='Company Name')
    email_id = models.CharField(max_length=300, null=True, blank=True, verbose_name='Email Id')
    contact_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='Contact Name')
    contact_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Contact Number')
    bank_detail = models.TextField(null=True, blank=True, verbose_name='Bank Details')
    HO_Contact = models.CharField(max_length=300,  null=True, blank=True, verbose_name='HO Contact Number')
    HO_address_and_branches = models.TextField(null=True, blank=True, verbose_name='HO addresss')
    HO_email = models.CharField(max_length=300, null=True, blank=True, verbose_name='HO Email Id')
    website = models.CharField(max_length=300, null=True, blank=True, verbose_name='Website')
    remark = models.TextField(null=True, blank=True, verbose_name='Remark')    
    supplier_images = models.ManyToManyField(SupplierImages, verbose_name='Supplier Images', blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Supplier Details'
        verbose_name_plural = 'Supplier Details'

class SalesPerson(models.Model):
    supplier = models.ForeignKey('SupplierDirectory', on_delete=models.CASCADE, related_name='SupplierSalesPerson')
    name = models.CharField(max_length=300, verbose_name='Sales Person')
    email_id = models.CharField(max_length=300, null=True, blank=True, verbose_name='Email Id')
    contact_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Contact Number')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sales Person'
        verbose_name_plural = 'Sales Persons'

