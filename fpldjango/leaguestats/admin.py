from django.contrib import admin

from .models import League, Player, PlayerGameweekStats, LeaguePlayers

admin.site.register(League)
admin.site.register(Player)
admin.site.register(PlayerGameweekStats)
admin.site.register(LeaguePlayers)
# Register your models here.
