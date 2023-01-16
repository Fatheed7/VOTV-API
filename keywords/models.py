from django.db import models
from django.contrib.postgres.fields import ArrayField


class Keywords(models.Model):
    kNumber = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    keywords = ArrayField(models.CharField(max_length=100, blank=True, null=True))
    # related_keywords = ArrayField(models.CharField(max_length=100, blank=True, null=True))

    class Meta:
        verbose_name_plural = "Keywords"

    def __str__(self):
        return self.name
