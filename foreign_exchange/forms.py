from django import forms
from django.forms import widgets
from .models import *

class ForeignExchangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ForeignExchangeForm, self).__init__(*args, **kwargs)

    class Meta:
        CHOICES = ((True, 'Active'),(False, 'InActive'))
        model = ForeignExchange
        exclude = ()

        widgets = {
            'currency_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter currency name'
                }
            ),
            'buy': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter buy rate'
                }
            ),
            'sale': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter sale rate'
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control'
                },
                choices = CHOICES
            )
        }
