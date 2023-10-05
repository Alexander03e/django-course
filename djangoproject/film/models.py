from django.db import models


# Create your models here.
class Films(models.Model):
    title = models.CharField('Фильм', max_length=50, default='')
    director = models.CharField('Режиссер', max_length=50, default='')
    actors = models.CharField('Актеры', max_length = 200, default = '')
    subtitle =  models.TextField('Описаниее')
    image = models.ImageField(upload_to='static/img/', verbose_name='Изображение')
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'