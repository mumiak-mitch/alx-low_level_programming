from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from listings.models import Listing, Town
from .forms import ListingForm, UpdateListingForm

# Create your views here.
#def home(request):
#    return render(request, 'index.html', {})

class HomeView(ListView):
    model = Listing
    template_name = "index.html"
    #ordering = ['-id']
    ordering = ['-date']

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

class DeleteListingView(DeleteView):
    model = Listing
    template_name = "delete_listing.html"
    success_url = reverse_lazy('home')


class AddTownView(CreateView):
    model = Town
    template_name = "add_town.html"
    fields = "__all__"