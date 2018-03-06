from django import forms
from django.forms import widgets
from tourproject import settings
from .models import *
import pdb

class SectorForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SectorForm, self).__init__(*args, **kwargs)
        self.fields['triptype'].empty_label = 'Select Trip Type'

    class Meta:
        model = Sector
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'sector_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter sector name'
                }
            ),
            'triptype': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control'                    
                },
                choices = CHOICES
            )
        }

        error_messages={
            'sector_name':{
                'required':'Please enter sector name.',
            },
            'status':{
                'required':'Please select status.'
            }
        }

class SupplierDepartureSeatInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control date_of_birth_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))
    passport_exp = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control passport_expiry_date', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SupplierDepartureSeatInfoForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = SupplierDetails.objects.filter(triptype__id = 1)
        self.fields['passport_exp'].required = False

    def clean(self):
        supplier = self.cleaned_data.get('supplier')
        # pdb.set_trace()        
        try:
            supplier_details = SupplierDetails.objects.get(id = supplier.id)
        except:
            supplier_details = None

        # raise validation error if available seat is 0 or None
        if supplier_details.departure_seat_availability is not None:
            if supplier_details.departure_seat_availability <= 0: 
                raise forms.ValidationError("Sorry, Seats are not available.")
        else:
            raise forms.ValidationError("Sorry, Seats are not available.")

        return self.cleaned_data

    # def save(self, commit=False):
    #     pdb.set_trace()        
    #     data = self.cleaned_data        
    #     self.cleaned_data['date_of_birth'] = data['date_of_birth'].strftime("%Y-%m-%d")  
    #     super(SupplierDepartureSeatInfoForm, self).save(commit=True)

    # def clean_date_of_birth(self):
    #     date_of_birth = self.cleaned_data.get('date_of_birth')
    #     pdb.set_trace()
    #     date_of_birth = date_of_birth.strftime("%Y-%m-%d")
    #     return date_of_birth

    class Meta:
        model = SupplierDepartureSeatInfo        
        exclude = ()

        widgets = {
            'supplier':  forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),
            'middle_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter middle name'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'mobile_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter mobile number'
                }
            ),
            # 'date_of_birth': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control date_of_birth_picker',
            #         'placeholder': 'dd-mm-yyyy',
            #     }
            # ),
            'passport_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter passport number'
                }
            ),
            # 'passport_exp': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control passport_expiry_date',
            #         'placeholder': 'Enter passport expiry date',
            #         'readonly': 'true'
            #     }
            # ),
            'booking_agent': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter booking agent name',
                }
            ),
            'rate_given': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter given rate'
                }
            )
        }
        
class SupplierReturnSeatInfoForm(forms.ModelForm):

    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control date_of_birth_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))
    
    passport_exp = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control passport_expiry_date', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SupplierReturnSeatInfoForm, self).__init__(*args, **kwargs)
        self.fields['passport_exp'].required = False
        self.fields['supplier'].queryset = SupplierDetails.objects.filter(triptype__id = 1)

    def clean(self):
        supplier = self.cleaned_data.get('supplier')
        try:
            supplier_details = SupplierDetails.objects.get(id = supplier.id)
        except:
            supplier_details = None

        # raise validation error if available seat is 0 or None
        if supplier_details.return_seat_availability is not None:
            if supplier_details.return_seat_availability <= 0: 
                raise forms.ValidationError("Sorry, Seats are not available.")
        else:
            raise forms.ValidationError("Sorry, Seats are not available.")

        return self.cleaned_data

    class Meta:
        model = SupplierReturnSeatInfo
        exclude = ()

        widgets = {
            'supplier':  forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),
            'middle_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter middle name'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'mobile_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter mobile number'
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs = {
                    'class': 'form-control date_of_birth_picker',
                    'placeholder': 'dd-mm-yyyy'
                }
            ),
            'passport_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter passport number'
                }
            ),
            'passport_exp': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter passport expiry date'
                }
            ),
            'booking_agent': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter booking agent name',
                }
            ),
            'rate_given': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter given rate'
                }
            )
        }

class SupplierDetailsForm(forms.ModelForm):
    departure_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control departure_date_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))    
    return_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control return_date_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))
    oneway_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control oneway_date_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SupplierDetailsForm, self).__init__(*args, **kwargs)
        self.fields['departure_seat_availability'].label = 'Dep. seat available'
        self.fields['return_seat_availability'].label = 'Ret. seat available'        
        self.fields['triptype'].empty_label = 'Select Trip'
        self.fields['sectors'].empty_label = 'Select Sector'
        self.fields['departure_date'].required = False
        self.fields['return_date'].required = False
        self.fields['oneway_date'].required = False
        self.fields['oneway_date'].label = 'One Way Date'
    # class Media:
    #     js = {
    #         'js/jquery-3.2.1.min.js',
    #         'js/supplier_scripts.js'
    #     }

    class Meta:
        model = SupplierDetails
        exclude = ()
        
        widgets = {
            'supplier_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter supplier name'
                }            
            ),
            'triptype': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'sectors': forms.Select(
                attrs = {
                    'class': 'form-control'  
                }
            ),
            'departure_time': forms.TextInput(
                attrs = {
                    'class': 'form-control timepicker',
                    'placeholder': 'HH:MM'
                }
            ),
            'departure_flt_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter departure flight no.'
                }
            ),
            'return_time': forms.TextInput(
                attrs = {
                    'class': 'form-control timepicker',
                    'placeholder': 'HH:MM'
                }
            ),
            'return_flt_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter return flight no.'
                }
            ),
            # 'departure_date': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control datepicker',
            #         'placeholder': 'yyyy-mm-dd'
            #     }
            # ),
            # 'return_date': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control datepicker',
            #         'placeholder': 'yyyy-mm-dd'
            #     }
            # ),
            'departure_seat_availability': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter available departure seats'
                }
            ),
            'return_seat_availability': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter available return seats'
                }
            ),
            'total_departure_seats': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter total departure seats'
                }
            ),
            'total_return_seats': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter total return seats'
                }
            ),
            'dep_rate_flash': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter departure rate for flash'
                }
            ),
            'ret_rate_flash': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter return rate for flash'
                }
            ),
            'other_details': forms.Textarea(
                attrs = {
                    'class': 'form-control'            
                }
            ),
            'dep_rate_supplier': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter departure rate by supplier'
                }
            ),
            'ret_rate_supplier': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter return rate by supplier'
                }
            ),
            'oneway_time': forms.TextInput(
                attrs = {
                    'class': 'form-control timepicker',
                    'placeholder': 'HH:MM'
                }
            ),
            # 'oneway_date': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control',
            #         'placeholder': 'Enter date for one way trip'
            #     }
            # ),
            'oneway_rate_supplier': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter rate for one way trip by supplier'
                }
            ),
            'oneway_seat_availability': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter available seat for one way trip'
                }
            ),
            'oneway_rate_flash': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter rate for flash'
                }
            ),
            'oneway_flt_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter one way flight no.'
                }
            ),
            'total_one_way_seats': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter total one way seats'
                }
            )
        }

class OneWaySeatForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control date_of_birth_picker', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))    
    passport_exp = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={'class':'form-control passport_expiry_date', 'placeholder': 'dd-mm-yyyy', 'readonly': 'true'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OneWaySeatForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = SupplierDetails.objects.filter(triptype__id = 2)
        self.fields['date_of_birth'].required = False
        self.fields['passport_exp'].required = False

    def clean(self):
        supplier = self.cleaned_data.get('supplier')        
        try:
            supplier_details = SupplierDetails.objects.get(id = supplier.id)
        except:
            supplier_details = None

        # raise validation error if available seat is 0 or None
        if supplier_details.oneway_seat_availability is not None:
            if supplier_details.oneway_seat_availability <= 0: 
                raise forms.ValidationError("Sorry, Seats are not available.")
        else:
            raise forms.ValidationError("Sorry, Seats are not available.")

        return self.cleaned_data


    class Meta:
        model = OneWaySeat
        exclude = ()

        widgets = {
            'supplier':  forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),
            'middle_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter middle name'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'mobile_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter mobile number'
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs = {
                    'class': 'form-control date_of_birth_picker',
                    'placeholder': 'dd-mm-yyyy'
                }
            ),
            'passport_no': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter passport number'
                }
            ),
            'passport_exp': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter passport expiry date'
                }
            ),
            'booking_agent': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter booking agent name',
                }
            ),
            'rate_given': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter given rate'
                }
            )
        }
