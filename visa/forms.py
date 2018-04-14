from django import forms
from django.forms import widgets
from .models import *

class PassportTrackTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PassportTrackTypeForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select Status'

    class Meta:
        model = PassportTrackType
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'track_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter tracking type'
                }
            ),
            'status': widgets.Select(
                attrs={
                    'class': 'form-control'
                },
                choices = CHOICES
            )
        }
    
class PassportTrackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PassportTrackForm, self).__init__(*args, **kwargs)
        self.fields['track_type'].empty_label = 'Select Type'
        self.fields['track_type'].queryset = PassportTrackType.objects.filter(status = True)

        class Meta:
            model = PassportTrack
            exclude = ()

            widgets={
                'passport_number': forms.TextInput(
                    attrs={
                        'class': 'form-control'
                    }
                ),
                'track_type': forms.Select(
                    attrs={
                        'class': 'form-control'
                    }
                ),
                'additional_details': forms.Textarea(
                    attrs={
                        'class': 'form-control'
                    }
                )
            }