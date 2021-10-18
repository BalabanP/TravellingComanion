from rest_framework import viewsets, status
from rest_framework.response import Response
from ...models import Trip
from ..serializers import *



class TripViewSet(viewsets.ViewSet):
    def list(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response (serializer.data)

    def create(self, request):
        serializer = TripSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        trip = Trip.objects.get(id=pk)
        serializer= TripSerializer(trip)
        return Response(serializer.data)

    def update(self, request, pk=None):
        trip = Trip.objects.get(id=pk)
        serializer= TripSerializer(instance=trip, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        trip = Trip.objects.get(id=pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
