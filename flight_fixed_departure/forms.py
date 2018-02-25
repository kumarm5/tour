from django import forms
from django.forms import widgets
from tourproject import settings
from .models import *
import pdb

class SectorForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SectorForm, self).__init__(*args, **kwargs)

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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SupplierDetailsForm, self).__init__(*args, **kwargs)
        self.fields['departure_seat_availability'].label = 'Dep. seat available'
        self.fields['return_seat_availability'].label = 'Ret. seat available'        
        
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
                    'class': 'form-control'
                }
            ),
            'total_return_seats': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'dep_rate_flash': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'ret_rate_flash': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'other_details': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'dep_rate_supplier': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'ret_rate_supplier': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
