from django.db import models

class RegistroHoras(models.Model):
    motivo = models.CharField(max_length=100, help_text="Motivo para as horas")

    def __str__(self):
        return self.motivo