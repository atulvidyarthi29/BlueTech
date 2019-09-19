from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # product_key = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
