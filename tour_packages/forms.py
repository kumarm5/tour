from django import forms
from django.forms import widgets
from .models import *
from ckeditor.widgets import CKEditorWidget

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
                    'placeholder': 'Enter title'
                }
            ),
            'tour_topic': widgets.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'tour_images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }


class PackageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PackageForm, self).__init__(*args, **kwargs)
        self.fields['tour'].empty_label = 'Select Tour'

    class Meta:
        model = TourPackages
        exclude = ()

        widgets = {
            'tour': widgets.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            'package_images': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class PackageImagesForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PackageImagesForm, self).__init__(*args, **kwargs)
        self.fields['package'].empty_label = 'Select Package'

    class Meta:
        model = PackageImages
        exclude = ()

        widgets = {
            'package': widgets.Select(
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
            'package_images': forms.FileInput(
                attrs = {
                    'class': 'form-control',
                }
            )
        }

class PackageDetailsForm(forms.ModelForm):
    overview = forms.CharField(widget=CKEditorWidget())
    inclusion = forms.CharField(widget=CKEditorWidget())
    exclusion = forms.CharField(widget=CKEditorWidget())
    how_to_book = forms.CharField(widget=CKEditorWidget())
    tour_info = forms.CharField(widget=CKEditorWidget())
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PackageDetailsForm, self).__init__(*args, **kwargs)
        self.fields['package'].empty_label = 'Select Package'

    class Meta:
        model = PackageDetails
        exclude = ()

        widgets = {
            'package': widgets.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter title'
                }
            ),
            # 'overview': forms.Textarea(
            #     attrs = {
            #         'class': 'form-control'
            #     }
            # ),
            'inclusion': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'exclusion': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'how_to_book': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'tour_info': forms.Textarea(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'map_image': forms.FileInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }