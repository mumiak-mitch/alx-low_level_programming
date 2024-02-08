from django import forms
from .models import Listing, Town

townChoices = Town.objects.all().values_list('towns','towns')
townchoice_list = []
for item in townChoices:
    townchoice_list.append(item)

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'owner', 'town', 'snippet', 'header_image', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business'}),
            #'owner': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner', 'value':'', 'id':'founder', 'type':'hidden'}),
            'town': forms.Select(choices=townchoice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One line summary'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brief description of the listing'}),
        }

class UpdateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'town', 'snippet', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The name of the business'}),
            'town': forms.Select(choices=townChoices, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One line summary'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Brief description of the listing'}),
        }