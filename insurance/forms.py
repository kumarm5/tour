from django import forms
from .models import *
from django.forms import widgets

class InsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InsuranceForm, self).__init__(*args, **kwargs)

    class Meta:
        models = Insurance
        exclude = ()

    widgets = {
        'images': forms.FileInput(
            attrs = {
                'class': 'form-control'
            }
        )
    }
    