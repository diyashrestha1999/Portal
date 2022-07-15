from .models import Client
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer


def getclientinfo(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
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
    
 
class ClientList(viewsets.ModelViewSet):

    queryset = Client.objects.filter(is_approved=True)
    serializer_class = ClientSerializer

