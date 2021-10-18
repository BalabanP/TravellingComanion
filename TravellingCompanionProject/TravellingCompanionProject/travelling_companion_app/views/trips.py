

from django.shortcuts import  render, redirect
from ..forms import TripForm
from django.contrib import messages
from ..models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
@login_required
def trip_detail(request, pk=None):
	trip=Trip.objects.get(id=pk)
	flights=Flight.objects.filter(trip=pk)
	bookings=Booking.objects.filter(trip=pk)
	context={
		'trip':trip,
		'flights':flights,
		'bookings':bookings
	}
	return render(request, 'trip_detail.html', context=context)



@login_required
def trip_create(request):
	if request.method == "POST":
		form = TripForm(request.POST)
		if form.is_valid():
			trip = Trip(
				name=form.data['name'],
				budget = form.data['budget'],
				currency = form.data['currency'],
				comments = form.data['comments'])
			trip.save()
			messages.success(request,"Trip is saved")
			return redirect('trip_detail/{}'.format(trip.id))
	form = TripForm()
	context ={
		'form':form,
	}
	return render(request, 
		'forms/trip.html',
		context=context)

@login_required
def trip_list(request):
	trips = Trip.objects.all()
	paginator = Paginator(trips, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render (
		request=request,
		template_name="main/trips.html",
		context={'trips':page_obj})

