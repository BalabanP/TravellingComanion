from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.admin.widgets import  FilteredSelectMultiple

# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = "__all__"
		widgets = {
				'date_from': DateInput(),
				'time_from':TimeInput(),
				'date_to': DateInput(),
				'time_to':TimeInput()
			}

class FlightForm(forms.ModelForm):
	
	class Meta:
		model = Flight
		fields = "__all__"
		widgets = {
				'date_from': DateInput(),
				'time_from':TimeInput(),
				'date_to': DateInput(),
				'time_to':TimeInput()
			}

class TripForm(ModelForm):
	class Meta:
		model = Trip
		fields = ['name', 'budget','currency', 'comments']
