from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os

class UsuarioCustom(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('GrupoArticulo', slugify(self.username), instance)
        return None

    STATUS = (
        ('regular', 'regular'),
        ('suscriptor','suscriptor'),
        ('moderador','moderador')
    )

    correo = models.EmailField(unique=True)
    estado = models.CharField(max_length=100, choices=STATUS, default='regular')
    descripcion = models.TextField('Descripción', max_length=600, default='', blank=True, null=True)
    image = models.ImageField(default='default/usuario.jpg', upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return  self.username


