from .models import Client
from django.shortcuts import render


def getclientinfo(request):
    if request.method == 'POST':
        first_name = request.POST["full_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        organisation = request.POST["organisation"]
        country = request.POST["country"]
        # print("helll", country)
        phone_number = request.POST["phone_number"]
        domain = request.POST["domain"]
        gender = request.POST["gender"]

        Client.objects.create(full_name=first_name,
                              last_name=last_name,
                              email=email,
                              organisation=organisation,
                              country=country,
                              phone_number=phone_number,
                              domain=domain,
                              gender=gender
                              )
    return render(request, "html/loginform.html")
