from django.contrib import admin
from .models import Tournament, Player, Captain, User, Availability, Match, Assign
from django.contrib.auth.admin import UserAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Captain)
admin.site.register(Availability)
admin.site.register(Match)
admin.site.register(Assign)
