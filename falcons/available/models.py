from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.utils import timezone


location = (
    ('Hefflinger Park-South', 'Hefflinger Park-South'),
    ('Hefflinger Park-North', 'Hefflinger Park-North'),
    ('NP Dodge Park', 'NP Dodge Park')
)

opponent = (
    ('Tigers', 'Tigers'),
    ('UNO Durangos', 'UNO Durangos'),
    ('NCC', 'NCC'),
    ('Riders', 'Riders'),
    ('Titans', 'Titans'),
    ('Komban', 'Komban'),
    ('Royals', 'Royals'),
    ('UNO Stallions', 'UNO Stallions')

)


class User(AbstractUser):
    @property
    def is_captain(self):
        if hasattr(self, 'captain'):
            return True
        return False

    @property
    def is_player(self):
        if hasattr(self, 'player'):
            return True
        return False


class Tournament(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Captain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name



class Match(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    time = models.TimeField()
    location = models.CharField(max_length=50, choices=location, blank=False)
    opponent = models.CharField(max_length=50, choices=opponent, blank=False)


    def __str__(self):
        return "Match on %s %s vs %s" % (self.date, self.time, self.opponent)


class Assign(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


    class Meta:
        unique_together = (('player', 'tournament'),)

    def __str__(self):
        cl = Tournament.objects.get(id=self.tournament_id)
        te = Player.objects.get(id=self.player_id)
        return '%s : %s' % (te.name, cl)



class Availability(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)


    def __str__(self):
        return "Availability for match %s: %s" % (self.match, self.availability)