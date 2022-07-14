from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client

# class UserSerializer(serializers.ModelSerializer):
#     # vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())
#     class Meta:
#         model=User
#         fields=['username','email']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields='__all__'
