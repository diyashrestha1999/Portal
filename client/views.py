from django import forms
from django.shortcuts import render
from countries_list import countries

# Create your views here.
class LoginForm(forms.Form):
    full_name= forms.CharField(label="First Name",max_length=50)
    last_name= forms.CharField(label="Last Name",max_length=50)
    email= forms.EmailField()
    oraganisation=forms.CharField(label="Organisation Name",max_length=50)
    country=forms.ChoiceField(choices=countries)
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(label="Phone Number",max_length=50)

def loginform(request):
    return render(request,'html/loginform.html',{"form":LoginForm()})