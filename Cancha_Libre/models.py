from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Jugador(models.Model):
    POSICIONES = [
        ('ARQ', 'Arquero'),
        ('DEF', 'Defensor'),
        ('MED', 'Mediocampista'),
        ('DEL', 'Delantero'),
    ]

    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=3, choices=POSICIONES, default='MED')
    skill = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5
    )

    def __str__(self):
        return f"{self.nombre} - {self.posicion} ({self.skill})"