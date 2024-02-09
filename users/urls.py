from django.urls import path
from .views import UserRegisterView, UserLogoutView, profileEditView, changePasswordView, PasswordChangeSuccess, ProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),

    path('logout_page/', UserLogoutView, name="logout_page"),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('edit_profile/', profileEditView.as_view(), name="edit_profile"),

    path('password/', changePasswordView.as_view(), name="password"),
    path('password-change-success/', PasswordChangeSuccess, name="password-change-success"),

    path('<int:pk>/profile/', ProfilePageView.as_view(), name="user_profile"),
]