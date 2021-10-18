
from django.shortcuts import  render, redirect
from ..forms import BookingForm, LocationForm
from django.contrib import messages
from ..models import *
from .utils import check_budget
from django.contrib.auth.decorators import login_required
@login_required
def location_create(request):
	if request.method == "POST":
		form = LocationForm(request.POST)
		if form.is_valid():
			location = Location(city=form.data['city'])
			location.save()
	form = LocationForm()
	return render(request, 'forms/location.html', {'form':form})

@login_required
def booking_create(request):
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			booking = Booking(
				trip=Trip.objects.get(id=form.data['trip']),
				location=Location.objects.get(id=form.data['location']),
				date_from=form.data['date_from'],
				date_to=form.data['date_to'],
				time_from=form.data['time_from'],
				time_to=form.data['time_to'],
				price=form.data['price'])
			if check_budget(form.data['trip'], form.data['price']):
				booking.save()
				return redirect('trip_detail/{}'.format(form.data['trip']))
			else: 
				messages.error(request,"Booking place is exceded Budget")
	elif request.method == "GET":
		form = BookingForm()
		return render(request, 'forms/booking.html', {'form':form})

@login_required
def booking_tripid(request, pk=None):
	if request.method == "GET":
		form = BookingForm(initial={'trip':pk})
		return render(request, 'forms/booking.html', {'form':form})
 

