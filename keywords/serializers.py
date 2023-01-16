from rest_framework import serializers
from .models import Keywords



class KeywordSerializer(serializers.ModelSerializer):

    # keywords = serializers.SerializerMethodField()

    class Meta:
        model = Keywords
        fields = [
            'id', 'kNumber', 'name', 'description', 'keywords'
        ]

    # def get_keywords(self, obj):
    #     return [
    #         Keywords.objects.filter(id=keyword).values_list('name', flat=True)
    #         for keyword in obj.related_keywords
    #     ]



class KeywordDetailSerializer(KeywordSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    id = serializers.ReadOnlyField(source='keywords.id')