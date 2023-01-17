from django.db import models
from django.contrib.postgres.fields import ArrayField


class Spell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=400, null=True)
    cooldown = models.IntegerField(null=True)
    source = models.CharField(max_length=100, null=True)
    encounter = models.CharField(max_length=100, null=True)
    gameClass = models.CharField(max_length=100, null=True)
    deck = models.CharField(max_length=100, null=True)
    keywords = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    relatedCards = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)