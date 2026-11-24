from rest_framework import serializers
from .models import Album, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'titulo', 'orden', 'duracion']
        read_only_fields = ['id']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'titulo', 'artista', 'tracks']
        read_only_fields = ['id']
