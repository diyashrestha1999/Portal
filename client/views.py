from .models import Client
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from .serializers import ClientCreateSerializer, ClientSerializer
from django.core.exceptions import ValidationError




class ClientCreateViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

    
 
class ClientList(viewsets.ModelViewSet):

    queryset = Client.objects.filter(is_approved=True)
    serializer_class = ClientSerializer

