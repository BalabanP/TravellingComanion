from rest_framework import viewsets, status
from rest_framework.response import Response
from ...models import Location
from ..serializers import *



class LocationViewSet(viewsets.ViewSet):
    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response (serializer.data)

    def create(self, request):
        serializer = LocationSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        location = Location.objects.get(id=pk)
        serializer= LocationSerializer(location)
        return Response(serializer.data)

    def update(self, request, pk=None):
        location = Location.objects.get(id=pk)
        serializer= LocationSerializer(instance=location, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        location = Location.objects.get(id=pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
