from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import flights, Passenger


# Create your views here.
def index(request):
    return render(request, "flights/layout.html", {
        "flights": flights.objects.all()
    })


def flight(request, flight_id):
    f = flights.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": f,
        "passengers": f.passengers.all(),
        "non_passenger": Passenger.objects.exclude(flights=f).all()
    })


def book(request, flight_id):
    f = flights.objects.get(pk=flight_id)
    if request.method == 'POST':
        f = flights.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passengers']))
        passenger.flights.add(f)
        return HttpResponseRedirect(reverse("flight", args=(f.id,)))
