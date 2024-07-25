from django.db import models
from django.urls import reverse

class Publicador(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacimiento = models.DateField(null=True, blank=True)
    bautismo = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Publicador'
        verbose_name_plural = 'Publicadores'

    def __str__(self):
        # Representación en cadena del objeto, útil para la administración
        return f"{self.nombre} {self.apellidos}"

    def save(self, *args, **kwargs):
        # Puedes añadir lógica personalizada aquí antes de guardar el objeto
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Retorna la URL para acceder a una instancia particular del modelo
        return reverse('publicador_detail', kwargs={'pk': self.pk})
