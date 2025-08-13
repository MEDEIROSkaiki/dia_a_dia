# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    event_time = models.TimeField(
        help_text="Hora em que o evento ocorreu (formato HH:MM)",
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        help_text="Onde o evento ocorreu",
        null=True,
        blank=True
    )

    # NOVO CAMPO PARA A IMAGEM
    image = models.ImageField(
        upload_to='recipes/images/',  # Subpasta dentro de 'media' para organizar os uploads
        help_text="Imagem do evento",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title