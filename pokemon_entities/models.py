from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField('рус назавние', max_length=200)
    title_en = models.CharField('анг назавние', max_length=200, blank=True, null=True)
    title_jp = models.CharField('яп назавние', max_length=200, blank=True, null=True)
    image = models.ImageField('изображение покемона', blank=True, null=True)

    description = models.TextField('описание покемона', blank=True, null=True)
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_evolutions", verbose_name='предыдущая эволюция покемона')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='entities', null=True)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления')
    disappeared_at = models.DateTimeField('время исчезновения')
    level = models.IntegerField('уровень', blank=True, null=True)
    health = models.IntegerField('здоровье', blank=True, null=True)
    strength = models.IntegerField('сила', blank=True, null=True)
    defence = models.IntegerField('защита', blank=True, null=True)
    stamina = models.IntegerField('выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon} {self.latitude} {self.longitude}'
