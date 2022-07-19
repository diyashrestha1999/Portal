from .models import Client
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from .serializers import ClientCreateSerializer, ClientSerializer
from django.core.exceptions import ValidationError


def getclientinfo(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        if Client.objects.filter(email=email).exists():
            raise ValidationError("Email already exist")
        organisation = request.POST["organisation"]
        country = request.POST["country"]
        phone_number = request.POST["phone_number"]
        domain = request.POST["domain"]
        gender = request.POST["gender"]
        Client.objects.create(first_name=first_name,
                              last_name=last_name,
                              email=email,
                              organisation=organisation,
                              country=country,
                              phone_number=phone_number,
                              domain=domain,
                              gender=gender
                              )
    return render(request, "html/loginform.html")

class ClientCreateViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

    
 
class ClientList(viewsets.ModelViewSet):

    queryset = Client.objects.filter(is_approved=True)
    serializer_class = ClientSerializer

