from django.shortcuts import render
from .models import flights


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": flights.objects.all()
    })
