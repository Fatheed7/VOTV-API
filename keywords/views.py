from rest_framework import generics
from .models import Keywords
from .serializers import KeywordSerializer, KeywordDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import filters


class KeywordList(generics.ListAPIView):
    serializer_class = KeywordSerializer
    queryset = Keywords.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'description']

class KeywordDetail(generics.RetrieveAPIView):
    serializer_class = KeywordDetailSerializer
    queryset = Keywords.objects.all()
    lookup_field = 'id'