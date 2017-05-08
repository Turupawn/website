from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from bitfield import BitField
from games.models import Game

class Stat(models.Model):
    """Ingame API Stat"""
    game = models.ForeignKey(Game)
    STAT_TYPE = (
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('average', 'Average'),
    )
    type = BitField(flags=STAT_TYPE)
    name = models.CharField(max_length=200)
    increment_only = models.BooleanField(default=False)
    max_change = models.PositiveIntegerField(null=True, blank=True)
    min_change = models.PositiveIntegerField(null=True, blank=True)
    max_value = models.PositiveIntegerField(null=True, blank=True)
    window = models.PositiveIntegerField(null=True, blank=True)
    default_value = models.IntegerField(null=True, blank=True)
    aggregated = models.IntegerField(null=True, blank=True)

class UserStat(models.Model):
    """Ingame API User Stat"""
    value = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    stat = models.ForeignKey(Stat)

class Achievement(models.Model):
    """Ingame API Achievement"""
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True)
    achieved_icon = models.ImageField(upload_to='achievements/achieved_icon', blank=True)
    unachieved_icon = models.ImageField(upload_to='achievements/unachieved_icon', blank=True)
    stat = models.ForeignKey(Stat, blank=True, null=True)

class UserAchievement(models.Model):
    """Ingame API User Achievement"""
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    achievement = models.ForeignKey(Achievement)
