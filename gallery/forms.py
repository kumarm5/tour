from django import forms
from django.forms import widgets
from .models import *

class GalleryMenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(GalleryMenuForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Select Status'

    class Meta:
        model = GalleryMenu
        CHOICES=((True,'Active'),(False,'Inactive'))
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title',
                }
            ),
            'status': widgets.Select(
                attrs = {
                    'class': 'form-control',
                },
                choices = CHOICES
            )
        }


class GallerySubCatForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(GallerySubCatForm, self).__init__(*args, **kwargs)
        self.fields['gallery_topic'].empty_label = 'Select Topic'

    class Meta:
        model = GallerySubCat
        exclude = ()

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'gallery_topic': widgets.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'sub_category_images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }

class GallerySubCatImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(GallerySubCatImageForm, self).__init__(*args, **kwargs)
        self.fields['sub_category'].empty_label = 'Select Category'

    class Meta:
        model = GalleryImages
        exclude = ()

        widgets = {
            'sub_category': widgets.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title',
                }
            ),
            'images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }