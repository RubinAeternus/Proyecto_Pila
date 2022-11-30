from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Articulo, GrupoArticulo, Comentario, Genero, creador
from .decorators import user_is_superuser
from .forms import comentarioForm
from django.shortcuts import render, get_object_or_404
from .forms import GrupoCrearForm, ArticuloCrearForm, GrupoUpdateForm, ArticuloUpdateForm, comentarioForm, GeneroCrearForm, CreadorCrearForm
# Create your views here.

def homepage(request):
    matching_series = GrupoArticulo.objects.all()

    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_series, 
        "type": "grupos"}
        )



def grupos (request, grupos: str):
    matching_series = Articulo.objects.filter(grupo__campo=grupos).all()

    

    return render(
        request=request,
        template_name='main/home.html',
        context={"objects":matching_series,
        "type":"articulo"},
        )


def articulo (request, grupos: str, articulo: str):
    matching_articulo = Articulo.objects.filter(grupo__campo=grupos, articulo_campo=articulo).first()
    

    return render(
        request=request,
        template_name='main/articulo.html',
        context={"object":matching_articulo}
        
        )

def genero (request, grupos: str, genero: str):
    matching_genero = genero.objects.filter(grupo__campo=grupos, genero_campo=genero).first()
    return render(
        request=request,
        template_name='main/genero.html',
        context={"object":matching_genero}
        
        )

def Creador (request, grupos: str, creador: str):
    matching_creador = creador.objects.filter(creador__campo=grupos, creador_campo=creador).first()
    return render(
        request=request,
        template_name='main/genero.html',
        context={"object":matching_creador}
        
        )



@user_is_superuser
def nuevo_grupo(request):
    if request.method == 'POST':
        form = GrupoCrearForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = GrupoCrearForm()

    return render(
        request=request,
        template_name='main/nueva_entrada.html',
        context={
            "object": "Grupos",
            "form": form
            }
        )
@user_is_superuser
def nuevo_post(request):
    if request.method == "POST":
        form = ArticuloCrearForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['grupo'].campo}/{form.cleaned_data.get('articulo_campo')}")

    else:
         form = ArticuloCrearForm()

    return render(
        request=request,
        template_name='main/nueva_entrada.html',
        context={
            "object": "Articulo",
            "form": form
            }
        )

@user_is_superuser
def nuevo_genero(request):
    if request.method == "POST":
        form = GeneroCrearForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['grupo'].campo}/{form.cleaned_data.get('autor')}")

    else:
         form = GeneroCrearForm()

    return render(
        request=request,
        template_name='main/nuevo_genero.html',
        context={
            "object": "Genero",
            "form": form
            }
        )

@user_is_superuser
def nuevo_creador(request):
    if request.method == "POST":
        form = CreadorCrearForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['grupo'].campo}/{form.cleaned_data.get('autor')}")

    else:
         form = CreadorCrearForm()

    return render(
        request=request,
        template_name='main/nuevo_creador.html',
        context={
            "object": "Creador",
            "form": form
            }
        )





@user_is_superuser
def grupos_update(request, grupos):
    matching_series = GrupoArticulo.objects.filter(campo=grupos).first()

    if request.method == "POST":
        form = GrupoUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    else:
        form = GrupoUpdateForm(instance=matching_series)

        return render(
            request=request,
            template_name='main/nueva_entrada.html',
            context={
                "object": "Grupos",
                "form": form
                }
            )

@user_is_superuser
def grupos_delete(request, grupos):
    matching_series = GrupoArticulo.objects.filter(campo=grupos).first()

    if request.method == "POST":
        matching_series.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='main/borrar_confirmar.html',
            context={
                "object": matching_series,
                "type": "Grupos"
                }
            )

@user_is_superuser
def articulo_update(request, grupos, articulo):
        matching_article = Articulo.objects.filter(grupo__campo=grupos, articulo_campo=articulo).first()

       # if request.method == "POST":
        form = ArticuloUpdateForm(request.POST, request.FILES, instance=matching_article)

        if form.is_valid():
            form.save()
            return redirect(f'/{matching_article.grupo}')
    
        else:
            form = ArticuloUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nueva_entrada.html',
            context={
                "object": "Articulo",
                "form": form
                }
            )


@user_is_superuser
def articulo_delete(request, grupos, articulo):
    matching_article = Articulo.objects.filter(grupo__campo=grupos, articulo_campo=articulo).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='main/borrar_confirmar.html',
            context={
                "object": matching_article,
                "type": "Articulo"
                }
            )


