from django.contrib import admin
from .models import Artifact

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('number','name', 'description', 'rarity', 'artifact_class')

admin.site.register(Artifact, ArtifactAdmin)
