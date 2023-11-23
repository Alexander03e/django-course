from django.contrib import admin
from .models import Films, Director, Genre

# Register your models here.


class FilmsCategory(admin.ModelAdmin):
    list_display = ('id','title', 'get_genre')
    list_filter = ['direct','genre']
    list_display_links=['title']
    

class DirectorId(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Films, FilmsCategory)
admin.site.register(Director, DirectorId)
admin.site.register(Genre)