from django.contrib import admin
from.models import Articulo, GrupoArticulo, Comentario, creador, Genero

class GrupoArticuloAdmin(admin.ModelAdmin):
    fields = [
        'titulo',
        'subtitulo',
        'campo',
        'publicacion',
        'autor',
        'image',
    ]

class ArticuloAdmin(admin.ModelAdmin):
    fields = [
        'titulo',
        'subtitulo',
        'articulo_campo',
        'contenido',
        'notas',
        'publicacion',
        'modificacion',
        'grupo',
        'autor',
        'image',
    ]

class GeneroAdmin(admin.ModelAdmin):
    fields = [
        'titulo', 
        'subtitulo', 
        'grupo', 
        'autor',
        'contenido',]

class CreadorAdmin(admin.ModelAdmin):
    fields = [
        'nombre', 
        'genero', 
        'grupo', 
        'biografia',
        'image',]

# Register your models here.

admin.site.register(GrupoArticulo, GrupoArticuloAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario)
admin.site.register(creador, CreadorAdmin)
admin.site.register(Genero, GeneroAdmin)
