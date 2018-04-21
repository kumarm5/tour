from django import forms
from .models import *

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