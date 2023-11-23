from django.db import models


# Create your models here.

class Director(models.Model):
    name=models.CharField('Режиссер', max_length=100, default='')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Режиссер'
        verbose_name_plural = 'Режиссеры'

class Genre(models.Model):
    name=models.CharField('Жанр', max_length=50, default ='')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Жанр'
        verbose_name_plural = 'Жанры'

class Films(models.Model):
    title = models.CharField('Фильм', max_length=50, default='') 
    actors = models.CharField('Актеры', max_length = 200, default = '')
    subtitle =  models.TextField('Описаниее')
    image = models.ImageField(upload_to='static/img/', verbose_name='Изображение')
    is_favorite = models.BooleanField(default=False)
    direct = models.ManyToManyField(Director, verbose_name='Режиссер')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    
    def get_genre(self):
        return ",".join([str(p) for p in self.genre.all()])
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    


