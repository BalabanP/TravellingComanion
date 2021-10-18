from rest_framework import viewsets, status
from rest_framework.response import Response
from ...models import  Booking
from ..serializers import *



class BookingViewSet(viewsets.ViewSet):
    def list(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response (serializer.data)

    def create(self, request):
        serializer = BookingSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        booking = Booking.objects.get(id=pk)
        serializer= BookingSerializer(booking)
        return Response(serializer.data)

    def update(self, request, pk=None):
        booking = Booking.objects.get(id=pk)
        serializer= BookingSerializer(instance=booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        booking = Booking.objects.get(id=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
