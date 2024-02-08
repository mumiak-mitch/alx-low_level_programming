from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

def UserLogoutView(request):
    return render(request, "registration/logout.html")

class profileEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class changePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name="registration/change-password.html"
    success_url = reverse_lazy('password-change-success')

def PasswordChangeSuccess(request):
    return render(request, "registration/pass-change-success.html")