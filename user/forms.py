from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    phone_number=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)

class Meta:   
    model =User
    fields=['username', 'email', 'phone_no', 'password', 'password2']
     

