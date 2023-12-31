# Generated by Django 4.2.5 on 2023-10-07 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0006_genre_films_genre'),
        ('hello', '0003_delete_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='film.films', verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
