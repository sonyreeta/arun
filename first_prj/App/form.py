from django import forms
from .models import Contact_Us
from .form import *


class ContactForm( forms.ModelForm):
    Name       =forms.CharField(max_length=100,label='Name', required=False,widget=forms.TextInput(attrs={'class':"form-control"}) )
    Email      =forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':"form-control"}))   
    Id         =forms.IntegerField(label='Id', widget=forms.TextInput(attrs={'class':"form-control"}))
    
    class Meta:
        model = Contact_Us
        fields = ('Name', 'Email', 'Id' )