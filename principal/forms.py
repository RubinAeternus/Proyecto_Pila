from django import forms
from .models import GrupoArticulo, Articulo, Comentario, Genero, creador

class GrupoCrearForm(forms.ModelForm):
    class Meta:
        model = GrupoArticulo

        fields = [
            "titulo",
            "subtitulo",
            "campo",
            "image",
        ]

class ArticuloCrearForm(forms.ModelForm):
    class Meta:
        model = Articulo

        fields = [
            "titulo",
            "subtitulo",
            "articulo_campo",
            "contenido",
            "notas",
            "grupo",
            "image",
        ]

class GeneroCrearForm(forms.ModelForm):
    class Meta:
        model = Genero

        fields = [
            "titulo",
            "subtitulo",
            "grupo",
            'autor',
            "contenido",
            
        ]


class CreadorCrearForm(forms.ModelForm):
    class Meta:
        model = creador

        fields = [
            "nombre",
            "genero",
            "grupo",
            'biografia',
            "genero",
            "image",
            
        ]

class GrupoUpdateForm(forms.ModelForm):
    class Meta:
        model = GrupoArticulo

        fields = [
            "titulo",
            "subtitulo",
            "image",
        ]

class ArticuloUpdateForm(forms.ModelForm):
    class Meta:
        model = Articulo

        fields = [
            "titulo",
            "subtitulo",
            "contenido",
            "notas",
            "grupo",
            "image",
        ]

class comentarioForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comentario
        fields = ('contenido', )