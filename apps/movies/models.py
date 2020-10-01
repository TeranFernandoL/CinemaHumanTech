from apps.behaviors import *


# Create your models here.
class Turn(TimesStampedModel, StateModel):
    schedule = models.TimeField(verbose_name='Horario', blank=True, null=True, unique=True)

    def __str__(self):
        return "{} - {} ".format(self.id, self.schedule)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class Movie(TimesStampedModel, StateModel):
    name = models.CharField(verbose_name='Nombres', blank=True, null=True, max_length=200)
    publication_date = models.DateField(verbose_name='Fecha de Publicacion', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='movie/image', blank=True, null=True)
    turns = models.ManyToManyField(Turn, verbose_name="turnos", blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"
