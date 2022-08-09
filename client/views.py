from .models import Client
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from .serializers import ClientCreateSerializer, ClientSerializer
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated




class ClientCreateViewSet(CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = []
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

    
 
class ClientList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.filter(is_approved=True)
    serializer_class = ClientSerializer
