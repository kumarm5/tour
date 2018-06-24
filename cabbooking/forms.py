from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.forms import widgets

class CitiesForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CitiesForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cities
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the city name'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ) 
        }

class VehicleMasterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VehicleMasterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleMaster
        exclude = ()

        widgets = {
            'vehicle_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the vehicle name'
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the category'
                }
            )
        }

class TermsAndConditionForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TermsAndConditionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TermsAndCondition
        exclude = ()

        widgets={
            'city': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class ExtraPickUpDropForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExtraPickUpDropForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select status'

    class Meta:
        model = ExtraPickUpDrop
        CHOICES=((True,'Available'),(False,'Booked'))
        exclude = ()

        widgets = {
            'routename': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter sector name'
                }
            ),
            'fromlocation': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'tolocation': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'vehiclename': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'vehicleimage': forms.FileInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'vehiclecategory': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Trip Type'
                }
            ),
            'vehicleprice': forms.TextInput(
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
