from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.models import User
from App_Login.models import UserProfile


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


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ('user',)







