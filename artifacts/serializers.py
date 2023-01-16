from rest_framework import serializers
from .models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artifact
        fields = [
            'number', 'name', 'description', 'rarity', 'artifact_class'
        ]


class ArtifactDetailSerializer(ArtifactSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    id = serializers.ReadOnlyField(source='artifact.number')