from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import ImageField
from .models import Profile



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email',]

    def __str__(self) -> str:
        return self.email + ', ' + self.username



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']