from rest_framework import serializers
from .models import Album, Track

<<<<<<< HEAD
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'titulo', 'orden', 'duracion']
        read_only_fields = ['id']

class AlbumSerializer(serializers.ModelSerializer):
=======

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'titulo', 'numero', 'duracion_segundos']


class AlbumSerializer(serializers.ModelSerializer):
    # Serializacion anidada (solo lectura) de las pistas del album
>>>>>>> origin/main
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
<<<<<<< HEAD
        fields = ['id', 'titulo', 'artista', 'tracks']
        read_only_fields = ['id']
=======
        fields = ['id', 'titulo', 'artista', 'anio', 'creado', 'tracks']
>>>>>>> origin/main
