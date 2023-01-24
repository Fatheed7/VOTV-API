from rest_framework import generics
from .models import Keywords
from .serializers import KeywordSerializer, KeywordDetailSerializer
from django_filters import rest_framework as filters

class KeywordFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    keywords = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Keywords
        fields = ['name', 'description', 'keywords']


class KeywordList(generics.ListAPIView):
    serializer_class = KeywordSerializer
    queryset = Keywords.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = KeywordFilter
    filterset_fields = ['name', 'description']

class KeywordDetail(generics.RetrieveAPIView):
    serializer_class = KeywordDetailSerializer
    queryset = Keywords.objects.all()
    lookup_field = 'id'