from django.contrib import admin

from .models import flights, Airport, Passenger

# Register your models here.
admin.site.register(flights)
admin.site.register(Airport)
admin.site.register(Passenger)
