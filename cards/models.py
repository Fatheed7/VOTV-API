from django.db import models
from django.contrib.postgres.fields import ArrayField


class Card(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gameClass = models.CharField(max_length=100, default='Global')
    type = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    rarity = models.CharField(max_length=100, default='Common')
    energy = models.CharField(max_length=2, null=True)
    upgradedEnergy = models.CharField(max_length=2, null=True)
    description = models.CharField(max_length=200, null=True)
    upgradedDescription = models.CharField(max_length=200, null=True)
    keywords = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    relatedCards = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    upgradedKeywords = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    upgradedRelatedCards = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.cName