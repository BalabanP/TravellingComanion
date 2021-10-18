from rest_framework import viewsets, status
from rest_framework.response import Response
from ...models import  Flight
from ..serializers import *

class FlightViewSet(viewsets.ViewSet):
    def list(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response (serializer.data)

    def create(self, request):
        serializer = FlightSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None):
        flight = Flight.objects.get(id=pk)
        serializer= FlightSerializer(flight)
        return Response(serializer.data)

    def update(self, request, pk=None):
        flight = Flight.objects.get(id=pk)
        serializer= FlightSerializer(instance=flight, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        flight = Flight.objects.get(id=pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
