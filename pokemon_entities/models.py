from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField('рус назавние', max_length=200)
    title_en = models.CharField('анг назавние', max_length=200, blank=True)
    title_jp = models.CharField('яп назавние', max_length=200, blank=True)
    image = models.ImageField('изображение покемона', blank=True)

    description = models.TextField('описание покемона', blank=True)
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_evolutions", verbose_name='предыдущая эволюция покемона')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления', default=timezone.now())
    disappeared_at = models.DateTimeField('время исчезновения', default=timezone.now())
    level = models.IntegerField('уровень', blank=True)
    health = models.IntegerField('здоровье', blank=True)
    strength = models.IntegerField('сила', blank=True)
    defence = models.IntegerField('защита', blank=True)
    stamina = models.IntegerField('выносливость', blank=True)
