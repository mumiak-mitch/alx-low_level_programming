from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from listings.models import UserProfile
from .forms import RegisterForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView

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


class ProfilePageView(DetailView):
    model = UserProfile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context