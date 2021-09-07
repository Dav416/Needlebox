from django.forms import *
from django import forms
from core.user.models import User


# ----Formulario para enviar correo de recuperar contraseña ------
class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su nombre de usuario',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        if not User.objects.filter(username=cleaned['username']).exists():
            # self._errors['error'] = self._errors.get('error', self.error_class())
            # self._errors['error'].append('El usuario no existe')
            raise forms.ValidationError('El usuario no existe')
        return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)


# ----Formulario para resetear contraseña ------
class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita el password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']
        if password != confirmPassword:
            # self._errors['error'] = self._errors.get('error', self.error_class())
            # self._errors['error'].append('El usuario no existe')
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return cleaned