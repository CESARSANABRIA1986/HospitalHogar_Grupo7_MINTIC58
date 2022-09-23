from django.db import models
from django.utils.translation import gettext_lazy as


class tipoPersona(models.model):
    class TipoUsuario(models.TextChoices):
        PACIENTE = 'PA', _('Paciente')
        ACUDIENTE = 'AC', _('Acudiente')
        MEDICO = 'MD', _('Medico')
    tipoUsuario= models.CharField(primary_key=True, max_length=3, choices=TipoUsuario.choices)
    permisos = models.models.IntegerField(default=0) 
