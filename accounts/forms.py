from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ Form used for creating a user """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """ Altering form used in admin interface to change user's info """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
