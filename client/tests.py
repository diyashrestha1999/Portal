from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Client

class TestClientModels(TestCase):
    def test_model_client(self):
        client = Client.objects.create(first_name="habin")
        expected_str = "Client: habin"
        self.assertEqual(str(client), expected_str)

class URLTests(TestCase):
    def test_api_url(self):
        
        # storing the response in the variable response
        url = reverse("main:api-root")
        response=self.client.get('/api/')

        # assertEqual is the method in the unit testCase class 
        self.assertEqual(response.status_code, 200)


class ClientTests(TestCase):
    def test_create_client(self):
        url = reverse('main:create')
        
        payload = {
            "first_name": "deeya",
            "last_name": "stha",
            "email": "ayid@gmail.com",
            "date": "2022-07-19",
            "domain": "aayulogic",
            "organisation": "aayulogic",
            "country": "AF",
            "phone_number": "9823443545",
            "gender": "Male",
            "organisation_size": "0-50 Employee"
        }
        response = self.client.post(path=url, data=payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Client.objects.filter(email="ayid@gmail.com"))

        payload["phone_number"] = "9823443546"
        payload["domain"] = "merojob"

        response = self.client.post(url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

     
        self.assertEqual(response.json().get('email')[0], "client with this email already exists.")
     
    
        payload["email"] = "AYId@gmail.com"

 

        response = self.client.post(url, data=payload, format='json')     
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('email')[0], "This 'EMAIL' already exists!.")

