from django.contrib.auth.models import User
from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    frame = models.ForeignKey("Frame", on_delete=models.CASCADE)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    tire = models.ForeignKey("Tire", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_basket = models.BooleanField()


class Order(models.Model):
    PENDING = 'P'
    READY = 'R'
    STATUS = [
        (PENDING, 'Pending'),
        (READY, 'Ready'),
    ]
    bike = models.ForeignKey("Bike", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS, default=PENDING)
