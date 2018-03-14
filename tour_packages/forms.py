from django import forms
from django.forms import widgets
from .models import *
import pdb

class TopicForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select Status'

    class Meta:
        model = Topics
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'topic': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter topic'
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control'                    
                },
                choices = CHOICES
            )
        }

        error_messages={
            'topic':{
                'required':'Please enter topic.',
            },
            'status':{
                'required':'Please select status.'
            }
        }

class TourForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TourForm, self).__init__(*args, **kwargs)
        self.fields['tour_topic'].empty_label = 'Select Topic'

    class Meta:
        model = Tours
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter topic'
                }
            ),
            'tour_topic': widgets.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'tour_images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
