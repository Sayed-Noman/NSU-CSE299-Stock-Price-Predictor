from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    '''
    This is a conceptual Form representation of class table for user signup
    :param UserCreationForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type UserCreationForm: model, fields

    '''
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    '''
    This is a conceptual Form representation of class table for user signin
    :param forms.Form: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type forms.Form: model, fields

    '''
    username = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "password"}))
    

    


