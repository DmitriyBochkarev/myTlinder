from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Friendship
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'gender', 'firstname', 'lastname']


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['from_friend', 'to_friend']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


