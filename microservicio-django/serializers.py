from rest_framework import serializers
from .models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'titulo', 'numero', 'duracion_segundos']


class AlbumSerializer(serializers.ModelSerializer):
    # Serializacion anidada (solo lectura) de las pistas del album
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'titulo', 'artista', 'anio', 'creado', 'tracks']
