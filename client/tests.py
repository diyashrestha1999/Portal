

import email
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Client

#testing example
class TestClientModels(TestCase):
    def test_model_client(self):
        client = Client.objects.create(first_name="habin")
        expected_str = "Client: habin"
        self.assertEqual(str(client), expected_str)

#testing whether api url is working or not 
class URLTests(TestCase):
    def test_api_url(self):
        
        #storing the url of api in the variable url --reverse function takes the url 
        url = reverse("main:api-root")

        # storing the response in the variable response
        response=self.client.get('/api/')

        # assertEqual is the method in the unit testCase class 
        self.assertEqual(response.status_code, 200)

#testing whether the post method is working or not
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

        #posting the data of payload in the api
        response = self.client.post(path=url, data=payload, format='json')

        #checking if the status of the response with the expected output
        self.assertEqual(response.status_code, 201)

        #checking if the filtered email exit or not
        self.assertEqual(Client.objects.filter(email="ayid@gmail.com").exists(), True)



       
     
        Client.objects.all().delete()
        

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
        response = self.client.post(url, data=payload, format='json')  
        self.assertEqual(response.status_code, 201)
        payload["phone_number"] = "9823443546"
        payload["domain"] = "merojob"
        payload["email"] = "Ayid@gmail.com"
      
        response = self.client.post(url, data=payload, format='json')  
        self.assertEqual(response.status_code, 400)
  
        # print(response.json())

       
        self.assertEqual(response.json().get('email')[0], "This 'EMAIL' already exists!.")
    

    def test_email_lowercase(self):
        url = reverse('main:create')

        payload = {
            "first_name": "deeya",
            "last_name": "stha",
            "email": "AAYULOGIC@gmail.com",
            "date": "2022-07-19",
            "domain": "aayulogic",
            "organisation": "aayulogic",
            "country": "AF",
            "phone_number": "9823443545",
            "gender": "Male",
            "organisation_size": "0-50 Employee"
        }

        response=self.client.post(url,data=payload, format='json')
        self.assertEqual(response.status_code, 201)

        #testing if the uppercase email is stored in lowercase email or not
        self.assertEqual(Client.objects.first().email, "aayulogic@gmail.com" )

   
    def test_phone_number(self):
        url = reverse('main:create')

        payload = {
            "first_name": "deeya",
            "last_name": "stha",
            "email": "AAYULOGIC@gmail.com",
            "date": "2022-07-19",
            "domain": "aayulogic",
            "organisation": "aayulogic",
            "country": "AF",
            "phone_number": "9823443545",
            "organisation_size": "0-50 Employee",
            "gender": "Male"
          
        }
        self.client.post(url, data=payload, format="json")


        payload["phone_number"]="9123443545"
        payload["email"]="diya@gmail.com"
        payload["domain"]="diya.com"

        response=self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, 400)
        
        self.assertEqual(response.json().get('phone_number')[0], "number should start with 98 or 97")


    def test_uniqueness(self):
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
        self.client.post(url, data=payload, format="json")

        #storing same dublicate data
        payload["email"]= "Ayid@gmail.com"

        payload["phone_number"]="9823443545"
     
        payload["domain"]= "aayulogic"

        response=self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, 400)
        print(response.json())

        self.assertEqual(response.json().get('phone_number')[0], 'client with this phone number already exists.')
        self.assertEqual(response.json().get('email')[0], "This 'EMAIL' already exists!.")
    
        self.assertEqual(response.json().get('domain')[0], 'client with this domain already exists.')







        

         