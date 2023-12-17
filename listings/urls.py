from django.urls import path
#from . import views
from .views import HomeView, ListingDetailView, AddListingView, UpdateListingView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('listings/<int:pk>/', ListingDetailView.as_view(), name="listings"),
    path('create_listing/', AddListingView.as_view(), name="create_listing"),
    path('listings/edit/<int:pk>/', UpdateListingView.as_view(), name="listings_update"),
]