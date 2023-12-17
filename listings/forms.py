from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'author', 'description', 'web_url', 'hours', 'date', 'start_time', 'end_time', 'social_media', 'logo', 'map_url', 'mobile_no', 'email', 'address', 'payment_method', 'other_info')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Provide detailed information about the listing.'}),
            'web_url': forms.URLInput(attrs={'class': 'form-control', 'required': False, 'placeholder':'optional'}),
            'hours': forms.TextInput(attrs={'class': 'form-control', 'required': False, 'placeholder':'optional'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': False}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': False}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': False}),
            'social_media': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'map_url': forms.URLInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Physical address, postal code might be added'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Provide other information that has not been included in the descripton section. If you do not have any just leave blank.'}),
        }

        labels = {
            'name': 'Business/Organization/Event/School Name',
            'web_url': 'Website',
            'hours': 'Operation Hours',
            'date': 'Event Date',
            'start_time': 'Opening Time/Start Time',
            'end_time': 'Closing Time/End Time',
            'social_media': 'Social Media Link',
            'logo': 'Photo/Logo',
            'map_url': 'Location Map',
            'other_info': 'Additional Information',
        }


class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'description', 'web_url', 'hours', 'date', 'start_time', 'end_time', 'social_media', 'logo', 'map_url', 'mobile_no', 'email', 'address', 'payment_method', 'other_info')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Provide detailed information about the listing.'}),
            'web_url': forms.URLInput(attrs={'class': 'form-control', 'required': False, 'placeholder':'optional'}),
            'hours': forms.TextInput(attrs={'class': 'form-control', 'required': False, 'placeholder':'optional'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': False}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': False}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': False}),
            'social_media': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'map_url': forms.URLInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Physical address, postal code might be added'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Provide other information that has not been included in the descripton section. If you do not have any just leave blank.'}),
        }

        labels = {
            'name': 'Business/Organization/Event/School Name',
            'web_url': 'Website',
            'hours': 'Operation Hours',
            'date': 'Event Date',
            'start_time': 'Opening Time/Start Time',
            'end_time': 'Closing Time/End Time',
            'social_media': 'Social Media Link',
            'logo': 'Photo/Logo',
            'map_url': 'Location Map',
            'other_info': 'Additional Information',
        }