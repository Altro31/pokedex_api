# Generated by Django 4.2.6 on 2023-10-06 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('evolve_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolve_to', to='pokedex.pokemon')),
                ('type_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokemon_type_1', to='pokedex.type')),
                ('type_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pokemon_type_2', to='pokedex.type')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
            },
        ),
    ]