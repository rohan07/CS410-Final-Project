from django import forms
from .models import user_mod
from django.contrib.auth.models import User


class Signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
