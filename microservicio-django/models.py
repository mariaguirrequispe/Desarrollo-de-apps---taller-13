from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"


class Track(models.Model):
    # Relacion 1:N con eliminacion en cascada
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    numero = models.PositiveIntegerField()
    duracion_segundos = models.PositiveIntegerField()

    class Meta:
        ordering = ['album', 'numero']

    def __str__(self):
        return self.titulo
