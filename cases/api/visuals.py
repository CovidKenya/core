from rest_framework import generics

from django.core.serializers import serialize

from cases.models import Country, Visual
from cases.serializers import VisualSerializer, CountrySerializer

class VisualList(generics.ListAPIView):
    queryset = Visual.objects.all()
    serializer_class = VisualSerializer

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer
	lookup_field = 'name'