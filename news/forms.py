from django import forms
from django.forms import widgets
from .models import *

class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(NewsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = NewsInfo
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title for news'
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control'                    
                },
                choices = CHOICES
            )
        }
