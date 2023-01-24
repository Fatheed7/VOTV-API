from rest_framework import generics
from .models import Spell
from .serializers import  SpellSerializer, SpellDetailSerializer
from django_filters import rest_framework as filters


class SpellFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    cooldown = filters.CharFilter(lookup_expr='icontains')
    source = filters.CharFilter(lookup_expr='icontains')
    encounter = filters.CharFilter(lookup_expr='icontains')
    gameClass = filters.CharFilter(lookup_expr='icontains')
    deck = filters.CharFilter(lookup_expr='icontains')
    keywords = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Spell
        fields = ['name', 'description', 'cooldown', 'source', 'encounter', 'gameClass', 'deck', 'keywords']

class SpellList(generics.ListAPIView):
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = SpellFilter
    filterset_fields = ['name', 'description', 'cooldown', 'source', 'encounter', 'gameClass', 'deck']

class SpellDetail(generics.RetrieveAPIView):
    serializer_class = SpellDetailSerializer
    queryset = Spell.objects.all()
    lookup_field = 'id'