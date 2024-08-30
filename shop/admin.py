from django.contrib import admin

# Register your models here.
from .models import Bike, Frame, Seat, Tire, Basket, Order

admin.site.register(Frame)
admin.site.register(Seat)
admin.site.register(Tire)
admin.site.register(Basket)
admin.site.register(Bike)
admin.site.register(Order)