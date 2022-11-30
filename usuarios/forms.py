from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm


class usuarioRegistroForm(UserCreationForm):
    correo = forms.EmailField(help_text='Se requiere de un correo valido', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'correo', 'password1', 'password2']
        
        def save(self, commit= True):
            user = super(usuarioRegistroForm, self).save(commit=False)
            user.correo = self.cleaned_data('correo')
            if commit:
                user.save()
                return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'correo','image', 'descripcion']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())