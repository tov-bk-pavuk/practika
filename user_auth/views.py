from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import NewUserForm


User = get_user_model


class CreateProfile(CreateView):
    template_name = 'registration/register.html'
    form_class = NewUserForm

    def form_valid(self, form):
        user = form.save()


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile_change.html'
    fields = ['username', 'email']
    #success_url =

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user