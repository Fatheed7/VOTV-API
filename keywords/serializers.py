from rest_framework import serializers
from .models import Keywords



class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keywords
        fields = [
            'id','name', 'description', 'keywords'
        ]


class KeywordDetailSerializer(KeywordSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    id = serializers.ReadOnlyField(source='keywords.id')