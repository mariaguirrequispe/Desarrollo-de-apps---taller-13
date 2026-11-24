from rest_framework.test import APITestCase
from .models import Album, Track

class CatalogoTests(APITestCase):
    def setUp(self):
        self.album = Album.objects.create(titulo='Prueba', artista='Equipo')
        self.track = Track.objects.create(album=self.album, titulo='Cancion', orden=1, duracion=180)

    def test_album_crud(self):
        r = self.client.post('/api/albumes/', {'titulo': 'Nuevo', 'artista': 'Artista'}, format='json')
        self.assertEqual(r.status_code, 201)
        url = f'/api/albumes/{r.data["id"]}/'
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.put(url, {'titulo': 'Editado', 'artista': 'Otro'}, format='json').status_code, 200)
        self.assertEqual(self.client.patch(url, {'titulo': 'Final'}, format='json').status_code, 200)
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_track_crud(self):
        r = self.client.post('/api/tracks/', {'album': self.album.id, 'titulo': 'Nueva', 'orden': 2, 'duracion': 200}, format='json')
        self.assertEqual(r.status_code, 201)
        url = f'/api/tracks/{r.data["id"]}/'
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.put(url, {'album': self.album.id, 'titulo': 'Editada', 'orden': 2, 'duracion': 220}, format='json').status_code, 200)
        self.assertEqual(self.client.patch(url, {'duracion': 230}, format='json').status_code, 200)
        self.assertEqual(self.client.delete(url).status_code, 204)

    def test_listas_y_anidamiento(self):
        r = self.client.get('/api/albumes/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data[0]['tracks'][0]['id'], self.track.id)
        self.assertEqual(self.client.get('/api/tracks/').status_code, 200)

    def test_cascada(self):
        self.assertEqual(self.client.delete(f'/api/albumes/{self.album.id}/').status_code, 204)
        self.assertFalse(Track.objects.filter(pk=self.track.id).exists())

    def test_album_inexistente(self):
        r = self.client.post('/api/tracks/', {'album': 999999, 'titulo': 'Invalida', 'orden': 1, 'duracion': 100}, format='json')
        self.assertEqual(r.status_code, 400)

    def test_duracion_invalida(self):
        r = self.client.patch(f'/api/tracks/{self.track.id}/', {'duracion': 0}, format='json')
        self.assertEqual(r.status_code, 400)

    def test_orden_repetido(self):
        r = self.client.post('/api/tracks/', {'album': self.album.id, 'titulo': 'Duplicada', 'orden': 1, 'duracion': 100}, format='json')
        self.assertEqual(r.status_code, 400)

    def test_sqlite_independiente(self):
        from django.conf import settings
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.sqlite3')
        self.assertEqual(Album.objects.get(pk=self.album.id).titulo, 'Prueba')
