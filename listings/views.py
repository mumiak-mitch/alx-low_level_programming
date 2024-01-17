from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from listings.models import Listing
from .forms import ListingForm

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