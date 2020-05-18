import json

from rest_framework import serializers

from .models import Country, Visual

class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = ['date', 'cases', 'deaths', 'recovered', 'last_updated']

class CountrySerializer(serializers.ModelSerializer):
    visuals = VisualSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['name', 'slug', 'visuals']

# class KenyanCaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KenyanCase
#         fields = '__all__'
