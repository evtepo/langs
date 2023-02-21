from django import forms
from .models import *

class SignIn(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    

