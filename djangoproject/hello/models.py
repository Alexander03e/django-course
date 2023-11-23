from django.db import models
from film.models import Films
from serials.models import Serials

# Create your models here.

class Recs(models.Model):
    name = models.ManyToManyField(Films, verbose_name='Рекомендованные фильмы')
    nameser = models.ManyToManyField(Serials, verbose_name='Рекомендованные сериалы', null=True)

    def get_rec(self):
        return ",".join([str(p) for p in self.rec.all()])
    class Meta:
        verbose_name = 'Рекомендации'
        verbose_name_plural = 'Рекомендации'
    