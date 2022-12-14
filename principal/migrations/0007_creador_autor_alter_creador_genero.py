# Generated by Django 4.1 on 2022-11-30 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0006_creador_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='creador',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creador',
            name='genero',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='principal.genero', verbose_name='Generos'),
        ),
    ]
