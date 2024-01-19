from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from listings.models import Listing
from .forms import ListingForm, UpdateListingForm

# Create your views here.
#def home(request):
#    return render(request, 'index.html', {})

class HomeView(ListView):
    model = Listing
    template_name = "index.html"

class ListingView(DetailView):
    model = Listing
    template_name = "listing_detail.html"

class AddListingView(CreateView):
    model = Listing
    template_name = "add_listing.html"
    #fields = "__all__"
    form_class = ListingForm

class UpdateListingView(UpdateView):
    model = Listing
    template_name = "update_listing.html"
    #fields = ['name', 'description']
    form_class = UpdateListingForm