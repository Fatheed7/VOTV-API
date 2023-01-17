from django.contrib import admin
from .models import Artifact

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'rarity', 'gameClass', 'keywords', 'relatedCards')

admin.site.register(Artifact, ArtifactAdmin)
