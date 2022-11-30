# Generated by Django 4.1 on 2022-11-28 23:47

from django.db import migrations, models
import principal.models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_genero_creador'),
    ]

    operations = [
        migrations.AddField(
            model_name='creador',
            name='image',
            field=models.ImageField(default='default/no_imagen.png', max_length=255, upload_to=principal.models.creador.image_upload_to),
        ),
    ]
