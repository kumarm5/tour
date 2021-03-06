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
        # self.fields['status'].empty_label = 'Select status'

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
                    'placeholder': 'Enter From Location'
                }
            ),
            'tolocation': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter To Location'
                }
            ),
            'vehiclename': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Vehicle Name'
                }
            ),
            'vehicleimage': forms.FileInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Vehicle Image'
                }
            ),
            'vehiclecategory': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Vehicle Category'
                }
            ),
            'vehicleprice': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Vehicle Price'
                }
            ),
            # 'action': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control',
            #     }
            # ),
            # 'status': widgets.Select(
            #     attrs = {
            #         'class': 'form-control'
            #     },
            #     choices = CHOICES
            # )
        }

class ExtraPickUpDropTermsForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExtraPickUpDropTermsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ExtraPickUpDropTerms
        exclude = ()

        widgets={
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            )
        }

class PickUpDropLiveTermsForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PickUpDropLiveTermsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PickUpDropLiveTerms
        exclude = ()

        widgets={
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            )
        }

class SharedLiveTermsForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SharedLiveTermsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SharedLiveTerms
        exclude = ()

        widgets={
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            )
        }


class PickDropLiveTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PickDropLiveTripForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select status'

    class Meta:
        model = PickDropLiveTrip
        CHOICES=((True,'Available'),(False,'Booked'))
        exclude = ()

        widgets={
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title' 
                }
            ),
            'status': widgets.Select(
                attrs={
                    'class': 'form-control'
                },
                choices=CHOICES
            )
        }