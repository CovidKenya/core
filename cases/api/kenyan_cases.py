from rest_framework import generics

from cases.models import KenyanCase
from cases.serializers import KenyanCaseSerializer


class KenyanCaseList(generics.ListAPIView):
    queryset = KenyanCase.objects.all()
    serializer_class = KenyanCaseSerializer
