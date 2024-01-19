from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'owner', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brief description of the listing'}),
        }

class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brief description of the listing'}),
        }