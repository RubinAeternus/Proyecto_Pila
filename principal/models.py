from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os

class GrupoArticulo (models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('GrupoArticulo', slugify(self.campo), instance)
        return None

    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, default="", blank=True)
    campo= models.SlugField("Campo", null=False, blank=False, unique=True)
    publicacion = models.DateTimeField("Fecha de publicacion ", default=timezone.now)
    autor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_imagen.png', upload_to=image_upload_to, max_length=255)

    def __str__(self):
       return self.titulo

    class Meta:
        verbose_name_plural = 'Grupos'
        ordering = ['-publicacion']

class Articulo(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('GrupoArticulo', slugify(self.grupo.campo), instance)
        return None
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, default="", blank=True)
    articulo_campo= models.SlugField("Campo de articulo", null=False, blank=False, unique=True)
    contenido = HTMLField(blank=True, default="")
    notas = HTMLField(blank=True, default="")
    publicacion = models.DateTimeField("Fecha de publicacion ", default=timezone.now)
    modificacion = models.DateTimeField("Fecha de modificacion", default=timezone.now)
    grupo = models.ForeignKey(GrupoArticulo, default="", verbose_name='Grupos', on_delete=models.SET_DEFAULT)
    autor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_imagen.png', upload_to=image_upload_to, max_length=255)

    def __str__(self):
       return self.titulo

    @property
    def campo(self):
       return self.grupo.campo + "/" + self.articulo_campo

    class Meta:
        verbose_name_plural = 'Articulo'
        ordering = ['-publicacion']

class Comentario (models.Model):
   post = models.ForeignKey('Articulo', on_delete=models.CASCADE)
   autor = models.CharField(max_length=200)
   fecha = models.DateField(auto_now_add=True)
   contenido = models.TextField()

   def __str__(self):
       return self.autor

class Genero (models.Model):
   titulo = models.CharField(max_length=200)
   subtitulo = models.CharField(max_length=200, default="", blank=True)
   grupo = models.ForeignKey(GrupoArticulo, default="", verbose_name='Grupos', on_delete=models.SET_DEFAULT)
   autor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
   contenido = HTMLField(blank=True, default="")

   def __str__(self):
       return self.titulo

   @property
   def campo(self):
       return self.grupo.campo 

   class Meta:
        verbose_name_plural = 'Genero'

class creador (models.Model):
   def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('GrupoArticulo', slugify(self.grupo.campo), instance)
        return None
   nombre = models.CharField(max_length=200)
   genero = models.CharField(max_length=200)
   grupo = models.ForeignKey(GrupoArticulo, default="", verbose_name='Grupos', on_delete=models.SET_DEFAULT)
   biografia = HTMLField(blank=True, default="")
   genero = models.ForeignKey(Genero, default="", verbose_name='Generos', on_delete=models.SET_DEFAULT)
   autor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
   image = models.ImageField(default='default/no_imagen.png', upload_to=image_upload_to, max_length=255)

   def __str__(self):
       return self.nombre

   @property
   def campo(self):
       return self.grupo.campo 

   class Meta:
        verbose_name_plural = 'Creador'
        

   
