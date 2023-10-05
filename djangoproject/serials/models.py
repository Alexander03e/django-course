from django.db import models

# Create your models here.
class Serials(models.Model):
    title = models.CharField('Сериал', max_length=50, default='')
    subtitle =  models.TextField('Описание')
    image = models.ImageField(upload_to='static/img/', verbose_name='Изображение')
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'