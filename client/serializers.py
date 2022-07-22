from dataclasses import field, fields
import email
from pyexpat import model
from django.contrib.auth.models import User
from django.forms import SlugField, ValidationError
from rest_framework import serializers
from .models import Client
import re



# class UserSerializer(serializers.ModelSerializer):
#     # vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())
#     class Meta:
#         model=User
#         fields=['username','email']

class ClientSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(read_only=True)
    class Meta:
        model= Client
        fields = ['first_name', 'last_name', 'email', 'date', 'domain']
        read_only_fields = fields


class ClientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'date', 'domain','organisation','country','phone_number','gender','date','organisation_size']

    def validate_domain(self, value):
        if Client.objects.filter(domain=value).exists():
            raise serializers.ValidationError("This 'DOMAIN' already exists!.")
        return value
        
    def validate_phone_number(self, value):
        if Client.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This 'NUMBER' already exists!.")
    
        if not re.match(r"9[7|8]\d{8}", value):
            raise serializers.ValidationError("number should start with 98 or 97")
        return value

    def validate_email(self, email):
        if Client.objects.filter(email=email.lower()).exists():
            raise serializers.ValidationError("This 'EMAIL' already exists!.")
        return email.lower()
