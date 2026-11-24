from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=150)
    artista = models.CharField(max_length=150)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.titulo} - {self.artista}'

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    orden = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    duracion = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['album_id', 'orden', 'id']
        constraints = [models.UniqueConstraint(fields=['album', 'orden'], name='track_orden_unico_por_album')]

    def __str__(self):
        return self.titulo
