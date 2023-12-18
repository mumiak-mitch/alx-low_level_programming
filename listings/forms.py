from django import forms
from .models import Listing, Category, Sub_County, Ward, Town

category_choices = Category.objects.all().values_list('categories', 'categories')
category_choicesList = []
for item in category_choices:
    category_choicesList.append(item)

subCounty_choices = Sub_County.objects.all().values_list('subCounties', 'subCounties')
subCounty_choicesList = []
for item in subCounty_choices:
    subCounty_choicesList.append(item)

ward_choices = Ward.objects.all().values_list('wards', 'wards')
ward_choicesList = []
for item in ward_choices:
    ward_choicesList.append(item)

town_choices = Town.objects.all().values_list('towns', 'towns')
town_choicesList = []
for item in town_choices:
    town_choicesList.append(item)


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'author', 'category', 'sub_county', 'ward', 'town', 'description', 'web_url', 'hours', 'date', 'start_time', 'end_time', 'social_media', 'logo', 'map_url', 'mobile_no', 'email', 'address', 'payment_method', 'other_info')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

            'category': forms.Select(choices=category_choicesList, attrs={'class': 'form-control'}),
            'sub_county': forms.Select(choices=subCounty_choicesList, attrs={'class': 'form-control'}),
            'ward': forms.Select(choices=ward_choicesList, attrs={'class': 'form-control'}),
            'town': forms.Select(choices=town_choicesList, attrs={'class': 'form-control'}),

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

            'category': forms.Select(choices=category_choicesList, attrs={'class': 'form-control'}),
            'sub_county': forms.Select(choices=subCounty_choicesList, attrs={'class': 'form-control'}),
            'ward': forms.Select(choices=ward_choicesList, attrs={'class': 'form-control'}),
            'town': forms.Select(choices=town_choicesList, attrs={'class': 'form-control'}),

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