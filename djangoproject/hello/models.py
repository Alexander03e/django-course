from django.db import models

# Create your models here.

class Liked(models.Model):
    title = models.CharField('Название', max_length=50)
    subtitle = models.TextField('Описаниее')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'