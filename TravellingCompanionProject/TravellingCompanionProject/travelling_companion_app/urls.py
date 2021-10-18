from django.urls import path, include
from .views import *
from . import api


app_name = "main"   


urlpatterns = [
    
    path("homepage", homepage, name="homepage"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("location_create", location_create, name="location_create"),
    path("booking_create", booking_create, name="booking_create"),
    path("booking/<int:pk>", booking_tripid, name="booking"),
    path("flight_create", flight_create, name="flight_create"),
    path("flight/<int:pk>", flight_tripid, name="flight"),
    path("trip_create", trip_create, name="trip_create"),
    path("trip_detail/<int:pk>", trip_detail, name="trip_detail"),
    path("trip-list", trip_list, name="trip_list"),

    path('v1/api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/api/locations/', api.location_list, name= 'location_list'),
    path('v1/api/locations/<int:pk>', api.location_detail, name= 'location_detail'),
    path('v1/api/flights/', api.flight_list, name= 'flight_list'),
    path('v1/api/flights/<int:pk>', api.flight_detail, name= 'flight_detail'),
    path('v1/api/trips/', api.trip_list, name= 'flight_list'),
    path('v1/api/trips/<int:pk>', api.trip_detail, name= 'flight_detail'),
    path('v1/api/bookings/', api.booking_list, name= 'flight_list'),
    path('v1/api/bookings/<int:pk>', api.booking_detail, name= 'flight_detail'),
]