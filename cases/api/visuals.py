from rest_framework import generics

from cases.models import Visual
from cases.serializers import VisualSerializer


class VisualList(generics.ListAPIView):
    queryset = Visual.objects.all()
    serializer_class = VisualSerializer
