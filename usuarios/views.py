from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import usuarioRegistroForm, UserLoginForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm
from .decorators import user_not_authenticated
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from .forms import SetPasswordForm
from .forms import PasswordResetForm
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string

from django.db.models.query_utils import Q

# Create your views here.

@user_not_authenticated
def registro(request):
   

    if request.method == "POST":
        form = usuarioRegistroForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            messages.success(request, f"Cuenta creada {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = usuarioRegistroForm()

    return render(
        request=request,
        template_name = "usuarios/registro.html",
        context={"form": form}
    )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect("homepage")

@user_not_authenticated
def custom_login(request):
    if request.user.is_authenticated:
        return redirect("homepage")

    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hola <b>{user.username}</b>! has ingresado exitosamente")
                return redirect("homepage")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="usuarios/login.html",
        context={"form": form}
        )

def perfil(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Su perfil ha sido actualizado')
            return redirect('perfil', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)


    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['descripcion'].widget.attrs = {'rows': 1}
        return render(request, 'usuarios/perfil.html', context={'form': form})

    return redirect("homepage")


    

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Su contraseña ha cambiado")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})

@user_not_authenticated
def password_reset_request(request):
    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    return redirect("homepage")
