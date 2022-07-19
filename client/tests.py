from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ClientTests(APITestCase):
    def test_create_client(self):
        url = reverse('main:create')
        
        data = {
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
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data["phone_number"] = "9823443546"
        data["domain"] = "merojob"
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get('email')[0], "client with this email already exists.")

        data["email"] = "AYID@gmail.com"
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get('email')[0], "This 'EMAIL' already exists!.")
        
