from django.urls import path
from .views import UserRegisterView, UserLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),

    path('logout_page/', UserLogoutView, name="logout_page"),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]