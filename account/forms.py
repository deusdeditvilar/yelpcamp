from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=15,widget=forms.TextInput(attrs={'class': 'yelp-input','placeholder':'johndoe_91'}),required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'yelp-input','placeholder':'Enter your Password'}))
    password2 = None

    class Meta:
        model = User
        fields = ('username',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=15,widget=forms.TextInput(attrs={'class': 'yelp-input','placeholder':'johndoe_91'}),required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'yelp-input','placeholder':'Enter your Password'}))

    class Meta:
        model = User
        fields = ('username',)