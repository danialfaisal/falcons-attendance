from django.contrib import admin
from .models import Player, Captain, User, Availability, Tournament, Match
from django.contrib.auth.admin import UserAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Player)
admin.site.register(Captain)
admin.site.register(Availability)
admin.site.register(Tournament)
admin.site.register(Match)