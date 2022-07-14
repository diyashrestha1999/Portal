from django.contrib.auth.password_validation import validate_password
from .models import Client
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from countries_list import countries
from .serializers import ClientSerializer
from rest_framework import viewsets


from django.core.validators import validate_slug

class ClientList(viewsets.ModelViewSet):

    queryset=Client.objects.all()
    serializer_class=ClientSerializer
# Create your views here.
CHOICE=[("Male","Male"),("Female","Female")]
class LoginForm(forms.Form):
    first_name= forms.CharField(label="First Name",max_length=50)
    last_name= forms.CharField(label="Last Name",max_length=50)
    email= forms.EmailField()
    organisation=forms.CharField(label="Organisation Name",max_length=50)
    country=forms.ChoiceField(choices=countries)
    phone_number = forms.CharField(label="Phone Number",max_length=50)
    domain=forms.CharField(validators=[validate_slug])

    gender=forms.ChoiceField(choices=CHOICE)

# def loginform(request):
#     return render(request,'html/loginform.html',{"form":LoginForm()})

def addClient(request):
    if request.method=="POST":
        value=LoginForm(request.POST)
        if value.is_valid():
            first_name=value.cleaned_data["first_name"]
            last_name=value.cleaned_data["last_name"]
            email=value.cleaned_data["email"]
            organisation=value.cleaned_data["organisation"]
            country=value.cleaned_data["country"]
            phone_number=value.cleaned_data["phone_number"]
            domain=value.cleaned_data["domain"]
            gender=value.cleaned_data["gender"]
            
        
            Client.objects.create(full_name=first_name,
            last_name=last_name,
            email=email,
            organisation=organisation,
            country=country,
            phone_number=phone_number,
            domain=domain,
            gender=gender
            )
        
       
            
            return HttpResponseRedirect(reverse("main:loginform"))
 
    return render(request,"html/loginform.html",{"form":LoginForm()})