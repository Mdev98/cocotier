from dataclasses import fields
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='usermame/email')
    password = forms.CharField(widget=forms.PasswordInput)