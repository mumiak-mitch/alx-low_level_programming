from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Listing
from .forms import ListingForm

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