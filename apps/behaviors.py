from django.db import models
from enum import Enum


class TimesStampedModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StateModel(models.Model):
    class State(Enum):
        ACTIVO = "ACTIVO"
        INACTIVO = "INACTIVO"

    state = models.CharField(verbose_name='Estado', blank=True, null=True, max_length=40,
                             choices=[(item.name, item.value) for item in State])

    class Meta:
        abstract = True
