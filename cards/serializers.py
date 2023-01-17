from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            'id', 'name', 'gameClass', 'type', 'rarity', 'energy', 'upgradedEnergy', 'description', 'upgradedDescription', 'keywords', 'relatedCards', 'upgradedKeywords', 'upgradedRelatedCards'
        ]


class CardDetailSerializer(CardSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    card = serializers.ReadOnlyField(source='card.id')