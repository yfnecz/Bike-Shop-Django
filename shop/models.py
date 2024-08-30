from django.contrib.auth.models import User
from django.db import models


# DecimalField, FloatField, IntegerField, BooleanField, CharField, TextField, DateField and FileField.
# price = models.DecimalField(max_digits=8, decimal_places=2)
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
    # There are other deleting strategies besides CASCADE: PROTECT, RESTRICT, SET_NULL, SET_DEFAULT, SET(), and DO_NOTHING
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


team_model_manager = Frame.objects

#falmouth_falcons = Team.objects.create(name="Falmouth Falcons")
#Player.objects.create(name="Karl Broadmoor", height=180, team=falmouth_falcons)
#Team.objects.filter(name="Ballycastle Bats")
#Player.objects.bulk_create([
#    Player(name="Karl Broadmoor", height=180, team=falmouth_falcons),
#    Player(name="Lennox Campbell", height=197, team=montrose_magpies)
#])
#falcons = Team.objects.get(name="Falmouth Falcons")
#falcon_player = Player.objects.get(team=falcons)
#try:
#    tornados = Team.objects.get(name="Tutshill Tornados")
#except Team.DoesNotExist:

#You will get not a player but a Player.MultipleObjectsReturned exception.
#great_score_at_home_games = Game.objects.filter(home_team_points__gt=12)

#tornados = Team.objects.filter(name="Tutshill Tornados")
#if len(tornados) == 1:
#    tornados_team = tornados[0]

#Team.objects.filter(name="Tutshill Tornados").count()
#team, created = Team.objects.get_or_create(name="Puddlemere United")
#if not Team.objects.filter(name="Puddlemere United").exists():

