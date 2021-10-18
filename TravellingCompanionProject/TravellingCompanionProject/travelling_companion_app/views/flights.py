
from django.shortcuts import  render, redirect
from ..forms import  FlightForm
from django.contrib import messages
from ..models import *
from .utils import check_budget
from django.contrib.auth.decorators import login_required
@login_required
def flight_create(request):
	if request.method == "POST":
		form = FlightForm(request.POST)
		if form.is_valid():
			flight = Flight(
				trip=Trip.objects.get(id=form.data['trip']),
				origin_location=Location.objects.get(id=form.data['origin_location']),
				destination=Location.objects.get(id=form.data['destination']),
				date_from=form.data['date_from'],
				date_to=form.data['date_to'],
				time_from=form.data['time_from'],
				time_to=form.data['time_to'],
				price=form.data['price'])
			if check_budget(form.data['trip'], form.data['price']):
				flight.save()
			else: 
				messages.error(request,"Flight is exceded Budget")
			return redirect('trip_detail/{}'.format(form.data['trip']))
	elif request.method == "GET":
		form = FlightForm()
		return render(request, 'forms/flight.html', {'form':form})
@login_required
def flight_tripid(request, pk=None):
	if request.method == "GET":
		form = FlightForm(initial={'trip':pk})
		return render(request, 'forms/flight.html', {'form':form})
