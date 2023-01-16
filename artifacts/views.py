from rest_framework import generics
from .models import Artifact
from .serializers import  ArtifactSerializer, ArtifactDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArtifactList(generics.ListAPIView):
    serializer_class = ArtifactSerializer
    queryset = Artifact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'rarity', 'artifact_class']

class ArtifactDetail(generics.RetrieveAPIView):
    serializer_class = ArtifactDetailSerializer
    queryset = Artifact.objects.all()
    lookup_field = 'id'