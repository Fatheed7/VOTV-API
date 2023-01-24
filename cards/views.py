from rest_framework import generics
from .models import Card
from .serializers import CardSerializer, CardDetailSerializer
from django_filters import rest_framework as filters

class CardFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    gameClass = filters.CharFilter(lookup_expr='icontains')
    rarity = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Card
        fields = ['name', 'gameClass', 'rarity']

class CardList(generics.ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = CardFilter
    filterset_fields = ['name', 'gameClass', 'rarity']

class CardDetail(generics.RetrieveAPIView):
    serializer_class = CardDetailSerializer
    queryset = Card.objects.all()
    lookup_field = 'id'


