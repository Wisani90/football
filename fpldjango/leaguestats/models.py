from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class League(models.Model):
    league_id = models.CharField(max_length=20)
    pub_time = models.DateTimeField('time published')

    def __str__(self):
        return self.league_id


@python_2_unicode_compatible
class Player(models.Model):
    player_id = models.CharField(max_length=20)
    name = models.CharField(max_length=128)
    team_name = models.CharField(max_length=128, default=None)
    pub_time = models.DateTimeField('time published', default=timezone.now)

    def __str__(self):
        return self.player_id


@python_2_unicode_compatible
class PlayerGameweekStats(models.Model):
    player_id = models.CharField(max_length=20)
    gameweek = models.CharField(max_length=20)
    gw_points = models.IntegerField()
    bench_points = models.IntegerField()
    transfers_made = models.IntegerField()
    transfers_cost = models.IntegerField()
    team_value = models.FloatField()
    overall_points = models.IntegerField(default=None)

    def __str__(self):
        return "%s %s" % (self.player_id, self.gameweek)


@python_2_unicode_compatible
class LeaguePlayers(models.Model):
    league = models.CharField(max_length=20)
    player = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.league, self.player)

