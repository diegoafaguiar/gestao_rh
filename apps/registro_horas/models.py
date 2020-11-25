from django.db import models
from apps.funcionarios.models import Funcionario

class RegistroHoras(models.Model):
    motivo = models.CharField(max_length=100, help_text="Motivo para as horas")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo