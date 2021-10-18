from ..models import Trip

def check_budget(trip_id, price):	
	trip=Trip.objects.get(id=trip_id),
	trip = list(trip)[0]
	trip.total_budget += int(price)
	if trip.total_budget > trip.budget:
		return False
	else: 
		trip.save()
		return True