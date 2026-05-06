from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Airline, Flight
from .serializers import AirlineSerializer, FlightSerializer


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all().order_by('id')
    serializer_class = AirlineSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all().order_by('id')
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['origin', 'destination', 'code']
