from django import forms
from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email')
        labels = {'email': 'Email Address'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }