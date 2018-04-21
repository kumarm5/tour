from django import forms
from django.forms import widgets
from .models import *
from ckeditor.widgets import CKEditorWidget

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

class VisaProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = 'Select User'

    class Meta:
        model = VisaProfile
        exclude = ()

        widgets = {
            'user': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'mobile_num': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the mobile number'
                }
            )
        }


class VisaCountryForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaCountryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VisaCountry
        exclude = ()

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter country name'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'details': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter details'
                }
            )
        }

class VisaInfoForm(forms.ModelForm):
    visa_details = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaInfoForm, self).__init__(*args, **kwargs)
        self.fields['visa_country'].empty_label = 'Select Country'

    class Meta:
        model = VisaInfo
        exclude = ()

        widgets = {
            'visa_country': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            # 'visa_details': forms.Textarea(
            #     attrs={
            #         'class': 'form-control'
            #     }
            # )
        }

class VisaDownloadsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaDownloadsForm, self).__init__(*args, **kwargs)
        self.fields['visa_country'].empty_label = 'Select Country'

    class Meta:
        model = VisaDownloads
        exclude = ()

        widgets={
            'visa_country': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class VisaEnquiryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaEnquiryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VisaEnquiry
        exclude = ()

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username'
                }
            ),
            'mobile_num': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter mobile number'
                }
            ),
            'email_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email id'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter subject'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter message'
                }
            )
        }

class VisaHistoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VisaHistoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VisaHistory
        exclude = ()
    
        widgets={
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username'
                }
            ),
            'mobile_num': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'mobile number'
                }
            ),
            'email_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email id'
                }
            ),
            'activity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter activity'
                }
            )
        }
