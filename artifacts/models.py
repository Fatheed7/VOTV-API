from django.db import models
from django.contrib.postgres.fields import ArrayField

class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True) 
    gameClass = models.CharField(max_length=100, null=True)
    rarity = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=400, null=True)
    keywords = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    relatedCards = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True)
    volatile = models.BooleanField(default=False, null=True)
    upgraded = models.BooleanField(default=False, null=True)


    class Meta:
        verbose_name_plural = "Artifacts"

    def __str__(self):
        return self.name
