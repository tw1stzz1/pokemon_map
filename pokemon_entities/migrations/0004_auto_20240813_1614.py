# Generated by Django 3.1.14 on 2024-08-13 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20240809_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='default title', max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='デフォルトのタイトル', max_length=200),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 13, 13, 14, 7, 822860, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 13, 13, 14, 7, 822860, tzinfo=utc)),
        ),
    ]
