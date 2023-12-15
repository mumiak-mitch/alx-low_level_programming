from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Listing

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Listing
    template_name = 'home.html'

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_details.html'