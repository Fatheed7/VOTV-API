from rest_framework import generics
from .models import Spell
from .serializers import  SpellSerializer, SpellDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SpellList(generics.ListAPIView):
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'cooldown', 'source', 'encounter', 'gameClass', 'deck']

class SpellDetail(generics.RetrieveAPIView):
    serializer_class = SpellDetailSerializer
    queryset = Spell.objects.all()
    lookup_field = 'id'