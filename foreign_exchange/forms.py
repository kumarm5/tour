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

class EnquiryDetailsForm(forms.ModelForm):
    sms_or_email_message = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EnquiryDetailsForm, self).__init__(*args, **kwargs)

    def clean(self):
        send_sms = self.cleaned_data['send_sms']
        send_email = self.cleaned_data['send_email']
        sms_or_email_message = self.cleaned_data['sms_or_email_message']

        if send_sms or send_email:
            if sms_or_email_message == '':
                self.add_error('sms_or_email_message', 'No sms or email message is given, Please specify message')
                # raise forms.ValidationError("No sms or email message is given, Please specify message")

        return self.cleaned_data

    class Meta:
        model = EnquiryDetails
        exclude = ()
