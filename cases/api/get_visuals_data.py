from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.services.get_cases import get_historical_data, get_local_data, get_yesterday_data

from cases.services.data import data

class UpdateVisualsData(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            get_historical_data()
        except Exception as error:
            raise APIException(f'Error: {error}')
        else:
            return Response("Data Updated")

class UpdateYesterDayVisualsData(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
           get_yesterday_data()
        except Exception as error:
            raise APIException(f'Error: {error}')
        else:
            return Response("Data Updated")
