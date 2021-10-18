from .views.api_auth import UserViewSet
from .views.booking import  BookingViewSet
from .views.flight import  FlightViewSet
from .views.location import LocationViewSet
from .views.trip import TripViewSet


location_list =LocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
location_detail = LocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

flight_list = FlightViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
flight_detail = FlightViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
booking_list = BookingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
booking_detail = BookingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
trip_list = TripViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
trip_detail = TripViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})