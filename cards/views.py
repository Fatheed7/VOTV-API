from rest_framework import generics
from .models import Card
from .serializers import CardSerializer, CardDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CardList(generics.ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cName', 'cNumber', 'cDesc', 'cDesc_Upgrade', 'cRarity', 'cType', 'cEnergy', 'cEnergy_Upgrade', 'keywords']