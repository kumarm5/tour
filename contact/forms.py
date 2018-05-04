from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class PreferredSalesAgentForm(forms.ModelForm):    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(PreferredSalesAgentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PreferredSalesAgent
        exclude = ()

        widgets = {
            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the company name'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the location'
                }
            ),
            'person_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the person name'
                }
            ),
            'contact_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the contact number'
                }
            ),
            'email_id':  forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the email id'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the address'
                }
            )
        }

class ContactInformationForm(forms.ModelForm):
    address = forms.CharField(widget=CKEditorWidget())
    banking = forms.CharField(widget=CKEditorWidget())
    companies = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(ContactInformationForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = ContactInformation
        exclude = ()
