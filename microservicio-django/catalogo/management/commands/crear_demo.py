from django.core.management.base import BaseCommand
from catalogo.models import Album, Track

class Command(BaseCommand):
    help = 'Crea un álbum y dos canciones de demostración sin duplicarlos.'
    def handle(self, *args, **options):
        album, _ = Album.objects.get_or_create(titulo='Demo Streaming', artista='Equipo Taller')
        for orden, titulo, duracion in [(1, 'Primera cancion', 180), (2, 'Segunda cancion', 210)]:
            Track.objects.get_or_create(album=album, orden=orden, defaults={'titulo': titulo, 'duracion': duracion})
        self.stdout.write(self.style.SUCCESS(f'Album id={album.id}; tracks={list(album.tracks.values_list("id", flat=True))}'))
