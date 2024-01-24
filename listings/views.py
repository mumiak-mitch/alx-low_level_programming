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
    
    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

class ListingView(DetailView):
    model = Listing
    template_name = "listing_detail.html"

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(ListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

class AddListingView(CreateView):
    model = Listing
    template_name = "add_listing.html"
    #fields = "__all__"
    form_class = ListingForm

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(AddListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

class UpdateListingView(UpdateView):
    model = Listing
    template_name = "update_listing.html"
    #fields = ['name', 'description']
    form_class = UpdateListingForm

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(UpdateListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context

class DeleteListingView(DeleteView):
    model = Listing
    template_name = "delete_listing.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(DeleteListingView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context


class AddTownView(CreateView):
    model = Town
    template_name = "add_town.html"
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        town_menu = Town.objects.all()
        context = super(AddTownView, self).get_context_data(*args, **kwargs)
        context["town_menu"] = town_menu
        return context
    
def TownView(request, specific_town):
    town_listings = Listing.objects.filter(town=specific_town)
    return render(request, "town.html", {'specific_town':specific_town.title(), 'town_listings':town_listings})

def TownListView(request):
    town_menulist = Town.objects.all()
    return render(request, "town_list.html", {'town_menulist':town_menulist})