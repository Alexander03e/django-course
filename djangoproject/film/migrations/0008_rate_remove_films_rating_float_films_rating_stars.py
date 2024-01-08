# Generated by Django 4.2.5 on 2023-11-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_films_rating_float_films_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
        migrations.RemoveField(
            model_name='films',
            name='rating_float',
        ),
        migrations.AddField(
            model_name='films',
            name='rating_stars',
            field=models.ManyToManyField(default=0, to='film.rate'),
        ),
    ]