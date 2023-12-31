# Generated by Django 4.2.5 on 2023-10-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0003_serials_director_serials_genre'),
        ('film', '0006_genre_films_genre'),
        ('hello', '0005_alter_recs_options_alter_recs_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recs',
            options={'verbose_name': 'Рекомендации', 'verbose_name_plural': 'Рекомендации'},
        ),
        migrations.AddField(
            model_name='recs',
            name='nameser',
            field=models.ManyToManyField(null=True, to='serials.serials', verbose_name='Рекомендованные сериалы'),
        ),
        migrations.AlterField(
            model_name='recs',
            name='name',
            field=models.ManyToManyField(to='film.films', verbose_name='Рекомендованные фильмы'),
        ),
    ]
