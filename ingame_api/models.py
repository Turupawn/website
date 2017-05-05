from __future__ import unicode_literals

from django.db import models
from bitfield import BitField

# Create your models here.

class Stat(models.Model):
    """Ingame API Stat"""
    value = models.IntegerField(null=True, blank=True) 
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

class Achievement(models.Model):
    """Ingame API Achievement"""
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True)
    achieved_icon = models.ImageField(upload_to='achievements/achieved_icon', blank=True)
    unachieved_icon = models.ImageField(upload_to='achievements/unachieved_icon', blank=True)
    stat = models.ForeignKey(Stat)
