from rest_framework import serializers
from .models import Airline, Flight


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['id', 'name', 'country']


class FlightSerializer(serializers.ModelSerializer):
    # 🔹 Lectura (GET), esto muestra objeto completo
    airline = AirlineSerializer(read_only=True)

    #Escritura (POST, PUT, PATCH), esto recibe recibe ID
    airline_id = serializers.PrimaryKeyRelatedField(
        queryset=Airline.objects.all(),
        source='airline',
        write_only=True
    )

    class Meta:
        model = Flight
        fields = [
            'id',
            'code',
            'origin',
            'destination',
            'airline',
            'airline_id'
        ]