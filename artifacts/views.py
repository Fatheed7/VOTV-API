from rest_framework import generics
from .models import Artifact
from .serializers import  ArtifactSerializer, ArtifactDetailSerializer
from django_filters import rest_framework as filters

class ArtifactFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    gameClass = filters.CharFilter(lookup_expr='icontains')
    rarity = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    keywords = filters.CharFilter(lookup_expr='icontains')
    relatedCards = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Artifact
        fields = ['name', 'gameClass', 'rarity', 'description', 'keywords', 'relatedCards']

class ArtifactList(generics.ListAPIView):
    serializer_class = ArtifactSerializer
    queryset = Artifact.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = ArtifactFilter
    filterset_fields = ['name', 'gameClass', 'rarity', 'description']

class ArtifactDetail(generics.RetrieveAPIView):
    serializer_class = ArtifactDetailSerializer
    queryset = Artifact.objects.all()
    lookup_field = 'id'