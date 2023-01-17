from rest_framework import serializers
from .models import Spell


class SpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = [
            'id', 'name', 'description', 'cooldown', 'source', 'encounter', 'gameClass', 'deck', 'keywords', 'relatedCards'
        ]


class SpellDetailSerializer(SpellSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    id = serializers.ReadOnlyField(source='spell.id')