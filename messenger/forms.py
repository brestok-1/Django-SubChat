from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm)
from django import forms
from django.contrib.auth.models import User

from messenger.models import Message, CustomUser


class CreateMessage(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Type your message', 'aria-describedby': "button-addon2"}),
        required=True)

    class Meta:
        model = Message
        fields = ['text']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter password',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter the password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password Confirmation'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
