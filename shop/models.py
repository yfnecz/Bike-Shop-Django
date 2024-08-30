from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"


class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"


class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type}"


class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity}"


class Bike(models.Model):
    frame = models.ForeignKey("Frame", on_delete=models.CASCADE)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    tire = models.ForeignKey("Tire", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_basket = models.BooleanField()

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"{self.name} {self.status}"

    def new_order(self):
        # need to update inventory
        frame = Frame.objects.get(id=self.bike.frame.id)
        frame.quantity -= 1
        frame.save()
        seat = Seat.objects.get(id=self.bike.seat.id)
        seat.quantity -= 1
        seat.save()
        if self.bike.has_basket:
            baskets = Basket.objects.first()
            baskets.quantity -= 1
            baskets.save()
        tires = Tire.objects.get(id=self.bike.tire.id)
        tires.quantity -= 2
        tires.save()
