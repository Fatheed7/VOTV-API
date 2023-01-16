from django.db import models
from keywords.models import Keywords
from sortedm2m.fields import SortedManyToManyField

# Create your models here.


class Card(models.Model):

    cRarity_CHOICES = [
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Affliction', 'Affliction'),
    ]
    
    cNumber = models.IntegerField()
    cDesc = models.CharField(max_length=100)
    cDesc_Upgrade = models.CharField(max_length=100)
    cRarity = models.CharField(max_length=20, choices=cRarity_CHOICES)
    cType = models.IntegerField()
    cName = models.CharField(max_length=100)
    cEnergy = models.IntegerField()
    cEnergy_Upgrade = models.IntegerField()
    keywords = SortedManyToManyField(Keywords, related_name='cards', blank=True)



    class Meta:
        ordering = ['cNumber']
    
    def __str__(self):
        return self.cName