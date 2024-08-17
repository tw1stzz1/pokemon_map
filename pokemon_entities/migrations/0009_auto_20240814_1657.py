# Generated by Django 3.1.14 on 2024-08-14 13:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20240814_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 14, 13, 57, 48, 336839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 14, 13, 57, 48, 336839, tzinfo=utc)),
        ),
    ]
