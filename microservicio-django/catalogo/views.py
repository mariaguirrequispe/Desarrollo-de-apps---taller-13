<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet
from .models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.prefetch_related('tracks').all()
    serializer_class = AlbumSerializer

class TrackViewSet(ModelViewSet):
=======
from rest_framework import viewsets
from .models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.prefetch_related('tracks').all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
>>>>>>> origin/main
    queryset = Track.objects.select_related('album').all()
    serializer_class = TrackSerializer
