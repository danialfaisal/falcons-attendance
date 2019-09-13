from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.utils import timezone


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


class Captain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name




class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_day = models.DateField(unique=True, db_index=True)
    match_time = models.TimeField()
    match_location = models.CharField(max_length=250)
    opponent = models.CharField(max_length=250)


    def __str__(self):
        return "Match at %s %s vs %s" % (self.match_day, self.match_time, self.opponent)


class Availability(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)

    class Meta:
        unique_together = ('match', 'player')

    def __str__(self):
        return "Availability for %s at match %s: %s" % (self.player, self.match, self.availability)