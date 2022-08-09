from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client
class DomainSuggestorAPIView(APIView):

    def post(self,request,*args,**kwargs):
        domain = self.request.data.get('domain')
        if not domain:
            return Response(
                {"data":"Domain is requried"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = {
            "is_available":not Client.objects.filter(domain__iexact=domain).exists()
        }

        return Response(response)