from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registro", views.registro, name="registro"),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('perfil/<username>', views.perfil, name ='perfil'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
]