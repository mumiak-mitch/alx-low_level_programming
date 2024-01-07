from django.shortcuts import render
from django.views.generic import ListView, DetailView
from listings.models import Listing

# Create your views here.
#def home(request):
#    return render(request, 'index.html', {})

class HomeView(ListView):
    model = Listing
    template_name = "index.html"

class ListingView(DetailView):
    model = Listing
    template_name = "listing_detail.html"