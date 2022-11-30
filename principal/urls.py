from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("nuevo_grupo", views.nuevo_grupo, name="crear-grupo"),
    path("nuevo_post", views.nuevo_post, name="crear-post"),
    path("nuevo_genero", views.nuevo_genero, name="crear-genero"),
    path("nuevo_creador", views.nuevo_creador, name="crear-creador"),
    path("<grupos>", views.grupos, name="grupos"),
    path("<grupos>/update", views.grupos_update, name="grupos_update"),
    path("<grupos>/delete", views.grupos_delete, name="grupos_delete"),
    path("<grupos>/<articulo>", views.articulo, name="articulo"),
    path("<grupos>/<genero>", views.Genero, name="genero"),
    path("<grupos>/<articulo>/update", views.articulo_update, name="articulo_update"),
    path("<grupos>/<articulo>/delete", views.articulo_delete, name="articulo_delete"),
    

]