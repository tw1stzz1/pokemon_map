from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, default='')
    title_jp = models.CharField(max_length=200, default='')
    image = models.ImageField(blank=True)

    description = models.TextField(default="")
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_evolution")

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(default=timezone.now(), blank=True)
    disappeared_at = models.DateTimeField(default=timezone.now(), blank=True)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
