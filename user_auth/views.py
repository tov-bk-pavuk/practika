from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import AuthenticationForm, LogoutView
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import NewUserForm, User
from blog.models import Article, Comment


def thanks(request):
    return render(request, 'registration/thanks.html')


def home(request):
    return render(request, 'base.html')


class CreateProfile(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = NewUserForm
    success_url = 'thanks'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    # form_class = UserChangeForm  # Либо поля либо форма
    template_name = 'registration/profile_change.html'
    fields = ['username', 'email']  # Либо поля либо форма
    success_url = 'thanks'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfilePublic(DetailView):
    model = User
    template_name = 'blog/user_profile.html'
    pk_url_kwarg = 'id'


class UserLogout(LogoutView):
    template_name = 'registration/logged_out.html'
