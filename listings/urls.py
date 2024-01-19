from django.urls import path
from .views import HomeView, ListingView, AddListingView, UpdateListingView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('listing/<int:pk>', ListingView.as_view(), name="listing"),
    path('add_listing', AddListingView.as_view(), name="add_listing"),
    path('update_listing/<int:pk>/update', UpdateListingView.as_view(), name="update_listing"),
]
