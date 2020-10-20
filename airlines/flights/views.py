from django.shortcuts import render
from .models import flights


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": flights.objects.all()
    })


def flight(request, flight_id):
    flight = flights.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })
