from django import forms
from .models import *

class FeedbackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        exclude = ()

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the name'
                }
            ),
            'mobile_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the number'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rating': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the rating'
                }
            ),
            'remark': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
