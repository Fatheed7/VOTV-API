from rest_framework import serializers
from .models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artifact
        fields = [
            'id', 'name', 'gameClass', 'rarity', 'description', 'keywords', 'relatedCards'
        ]


class ArtifactDetailSerializer(ArtifactSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    id = serializers.ReadOnlyField(source='artifact.number')