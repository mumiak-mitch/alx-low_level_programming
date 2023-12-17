from django.urls import path
from .views import MerchantRegisterView

urlpatterns = [
    path('mregister/', MerchantRegisterView.as_view(), name="merchant_register"),
]