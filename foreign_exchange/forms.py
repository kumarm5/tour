from django import forms
from django.forms import widgets
from .models import *
from ckeditor.widgets import CKEditorWidget

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