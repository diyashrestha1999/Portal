from dataclasses import field, fields
import email
from pyexpat import model
from django.contrib.auth.models import User
from django.forms import SlugField, ValidationError
from rest_framework import serializers
from .models import Client


# class UserSerializer(serializers.ModelSerializer):
#     # vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())
#     class Meta:
#         model=User
#         fields=['username','email']

class ClientSerializer(serializers.ModelSerializer):
    # domain = serializers.SerializerMethodField()
    class Meta:
        model= Client
        fields = ['first_name', 'last_name', 'email', 'date', 'domain']


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

        if not value.startswith("98"):
            raise serializers.ValidationError("bigriyo")
        return value

    def validate(self, attrs):
        email = attrs.get("email").lower()
        attrs["email"] = email
        if Client.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "This 'EMAIL' already exists!."})
        return super().validate(attrs)
