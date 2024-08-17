from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField('рус назавние', max_length=200)
    title_en = models.CharField('англ назавние', max_length=200, default='')
    title_jp = models.CharField('япон назавние', max_length=200, default='')
    image = models.ImageField('изображение покемона', blank=True)

    description = models.TextField('описание покемона',default="")
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_evolution", verbose_name='предыдущая эволюция покемона')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления', default=timezone.now(), blank=True)
    disappeared_at = models.DateTimeField('время исчезновения', default=timezone.now(), blank=True)
    level = models.IntegerField('уровень', default=1)
    health = models.IntegerField('здоровье', default=1)
    strength = models.IntegerField('сила', default=1)
    defence = models.IntegerField('защита', default=1)
    stamina = models.IntegerField('выносливость', default=1)
