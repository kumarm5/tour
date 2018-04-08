from django import forms
from .models import *

class CityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CityForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = City
        exclude = ()

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the city name'
                }
            ),
            'images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            ) 
        }

        error_messages = {
            'name': {
                'required': 'Please enter city name'
            },
            'images': {
                'required': 'Please select city name'
            }
        }

class HotelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HotelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Hotel
        exclude = ()

        widgets = {
            'city': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter hotel name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hotel_images': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class HotelImagesForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HotelImagesForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HotelImages
        exclude = ()

        widgets = {
            'hotel': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter the title'
                }
            ),
            'hotel_images': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class HotelDetailsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HotelDetailsForm, self).__init__(*args, **kwargs)
        self.fields['hotel'].empty_label = 'Select Hotel'

    class Meta:
        model = HotelDetails
        exclude = ()

        widgets = {
            'hotel': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'overview': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'inclusion': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'exclusion': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'how_to_book': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'hotel_info': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'map_image': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
                