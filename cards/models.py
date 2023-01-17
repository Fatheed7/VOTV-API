from django.db import models
from django.contrib.postgres.fields import ArrayField


class Card(models.Model):

    rarity_choices = {
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Affliction', 'Affliction'),
    }
    gameClass_choices = {
        ('The Hidden', 'The Hidden'),
        ('The Tempest', 'The Tempest'),
        ('The Enlightened', 'The Enlightened'),
        ('The Daughter of the Void', 'The Daughter of the Void'),
        ('Global', 'Global'),
    }

    type_choices = {
        ('Attack', 'Attack'),
        ('Ability', 'Ability'),
        ('Block', 'Block'),
        ('Heavy', 'Heavy'),
        ('Buff', 'Buff'),
        ('Affliction', 'Affliction'),
    }


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gameClass = models.CharField(max_length=100, choices=gameClass_choices, default='Global')
    type = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    rarity = models.CharField(max_length=100, choices=rarity_choices, default='Common')
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