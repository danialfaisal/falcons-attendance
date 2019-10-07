from django import forms
from django.http import HttpResponseRedirect
from .models import Captain, Player, Match, Availability, Assign, Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ('id', 'name',)


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('id', 'tournament', 'date', 'time', 'location', 'opponent',)

class AssignForm(forms.ModelForm):
   class Meta:
       model = Assign
       fields = ('tournament', 'player',)