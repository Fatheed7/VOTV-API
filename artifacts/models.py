from django.db import models

class Artifact(models.Model):
    artifact_class_CHOICES = [
        ('The Hidden', 'The Hidden'),
        ('The Tempest', 'The Tempest'),
        ('The Enlightened', 'The Enlightened'),
        ('The Daughter of the Void', 'The Daughter of the Void'),
        ('Global', 'Global'),
    ]
    rarity_CHOICES = [
        ('Starter', 'Starter'),
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Elite', 'Elite'),
    ]
    artifact_class = models.CharField(max_length=100, choices=artifact_class_CHOICES)
    number = models.IntegerField()
    rarity = models.CharField(max_length=20, choices=rarity_CHOICES)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Artifacts"

    def __str__(self):
        return self.name
