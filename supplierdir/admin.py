from django.contrib import admin
from .models import *
from .export_mixin import ExportCsvMixin
# Register your models here.

# admin.site.register(SupplierDirectory)

class SupplierImagesAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('supplier', 'title')
    fields = (('supplier','title'),('supplier_images'))
    
    actions = ["export_as_csv"]
    
admin.site.register(SupplierImages, SupplierImagesAdmin)


class SalesPersonInlineAdmin(admin.StackedInline):
    model = SalesPerson
    fk_name = 'supplier'
    fields = (('name','email_id'),('contact_number'),)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return 0
        else:
            return 1

class SupplierDirectoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('country', 'product', 'company_name', 'email_id', 'contact_name', 'contact_number')
    fields = (('country','product'),('company_name','email_id') , ('contact_name', 'contact_number'), ('website', 'supplier_images'),)
    inlines = [SalesPersonInlineAdmin,]
    
    actions = ["export_as_csv"]
    
admin.site.register(SupplierDirectory, SupplierDirectoryAdmin)


class SalesPersonAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'email_id', 'contact_number')
    fields = (('supplier','name'),('email_id','contact_number'),)
    
    actions = ["export_as_csv"]
    
admin.site.register(SalesPerson, SalesPersonAdmin)
