from django import forms
from .models import *

class TestimonialForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TestimonialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Testimonial
        exclude = ()

        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'address': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter address',
                }
            ),
            'images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'rating': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter rating'
                }
            )
        }