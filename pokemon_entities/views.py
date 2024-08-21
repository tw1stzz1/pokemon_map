import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    now = localtime()
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lt=now, disappeared_at__gt=now)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
        })    

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemon_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    previous_pokemon = requested_pokemon.previous_evolution
    previous_evolution = {}
    if previous_pokemon:
        previous_evolution = {
            'title_ru': previous_pokemon.title_ru,
            'pokemon_id': previous_pokemon.id,
            'img_url': previous_pokemon.image.url
        }

    next_pokemon = requested_pokemon.next_evolutions.first()
    next_evolution = {}
    if next_pokemon:
        next_evolution = {
            'title_ru': next_pokemon.title_ru,
            'pokemon_id': next_pokemon.id,
            'img_url': next_pokemon.image.url
        }

    pokemon_info = {
        'img_url': request.build_absolute_uri(requested_pokemon.image.url),
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
        'next_evolution': next_evolution,
        'previous_evolution': previous_evolution
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })
