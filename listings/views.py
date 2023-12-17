from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Listing
from .forms import ListingForm, UpdateListingForm

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Listing
    template_name = 'home.html'

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_details.html'

class AddListingView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'add_listing.html'
    #fields = '__all__'

class UpdateListingView(UpdateView):
    model = Listing
    template_name = 'update_listing.html'
    #fields = ('name', 'description', 'web_url', 'hours', 'date', 'start_time', 'end_time', 'social_media', 'logo', 'map_url', 'mobile_no', 'email', 'address', 'payment_method', 'other_info')
    form_class = UpdateListingForm