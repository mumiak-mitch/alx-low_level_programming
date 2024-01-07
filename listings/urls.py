from django.urls import path
from .views import HomeView, ListingView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('listing/<int:pk>', ListingView.as_view(), name="listing"),
]
