from rest_framework import serializers
from .models import Airline, Flight


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    airline_name = serializers.CharField(
        source='airline.name',
        read_only=True
    )

    class Meta:
        model = Flight
        fields = '__all__'