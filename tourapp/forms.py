from django import forms
from django.forms import widgets
from .models import HomeImageSlider

class HomeImageSliderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HomeImageSliderForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select Status'

    class Meta:
        model = HomeImageSlider
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description'
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control'                    
                },
                choices = CHOICES
            )
        }
        