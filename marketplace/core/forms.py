from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class SellerForm(forms.ModelForm):
    
    class Meta:
        model = Seller
        fields = ['First_Name', 'Last_Name', 'Product_Type', 'Experience', 'Introduction', 'Information', 'GroupChat', 'Questions']
    
    First_Name = forms.CharField(label="First Name", 
        widget=forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}), max_length=100, required=True)
    
    Last_Name = forms.CharField(label="Last name", 
        widget=forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}), max_length=100, required=True)
    
    Product_Type = forms.CharField(label="1. What do you plan on selling? Clothes/Handmade Items/Books/Art Supplies/Others...", 
        widget = forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}), max_length=255, required=True)
    
    Exp_choices = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    Experience = forms.ChoiceField(label="2. Do you have experience selling secondhand?", 
        widget=forms.RadioSelect, required= True, choices=Exp_choices)
    
    Introduction = forms.CharField(max_length=200, label="3. Introduce yourself: (Name, School, Age)", 
        required= True, widget= forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}))
    
    Information = forms.CharField(max_length=100, label="4. Contact Information (Wechat ID or Instagram)", 
        required= True, widget= forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}))
    
    GroupChat = forms.ChoiceField(label="5. Are you in the SASEXCHANGE group chat?", widget=forms.RadioSelect, 
        required= True, choices=Exp_choices)
    
    Questions = forms.CharField(max_length=200, label="6. Any Questions?", 
        widget= forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-lg'}), required=False)
    