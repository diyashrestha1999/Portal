from django.contrib.auth.password_validation import validate_password
from .models import Client
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from countries_list import countries
from django.contrib.auth import authenticate

# Create your views here.
class LoginForm(forms.Form):
    first_name= forms.CharField(label="First Name",max_length=50)
    last_name= forms.CharField(label="Last Name",max_length=50)
    email= forms.EmailField()
    oraganisation=forms.CharField(label="Organisation Name",max_length=50)
    country=forms.ChoiceField(choices=countries)
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(label="Phone Number",max_length=50)

# def loginform(request):
#     return render(request,'html/loginform.html',{"form":LoginForm()})

def addClient(request):
    if request.method=="POST":
        value=LoginForm(request.POST)
        if value.is_valid():
            first_name=value.cleaned_data["first_name"]
            last_name=value.cleaned_data["last_name"]
            email=value.cleaned_data["email"]
            oraganisation=value.cleaned_data["oraganisation"]
            country=value.cleaned_data["country"]
            password=value.cleaned_data["password"]
            retype_password=value.cleaned_data["retype_password"]
            phone_number=value.cleaned_data["phone_number"]
            if password==retype_password:
        
                Client.objects.create(full_name=first_name,
                last_name=last_name,
                email=email,
                oraganisation=oraganisation,
                country=country,
                password = password,
                phone_number=phone_number)
           
       
            
            return HttpResponseRedirect(reverse("main:loginform"))
 
    return render(request,"html/loginform.html",{"form":LoginForm()})