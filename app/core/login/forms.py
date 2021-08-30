from django.forms import *

from core.login.models import RegUsu


# -------------------------------
class RegistrarUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RegUsu
        fields = '__all__'
        widgets = {
            'nomComUsu': TextInput(
                attrs={
                    'id': 'NomCpl',
                    'placeholder': 'Nombre completo'
                }
            ),

            'e_mailUsu': EmailInput(
                attrs={
                    'id': 'EmlCl',
                    'placeholder': 'Correo'
                }
            ),

            'passwordUsu': PasswordInput(
                attrs={
                    'id': 'PassCl',
                    'placeholder': 'Contraseña'
                }
            ),

            'conf_passwordUsu': PasswordInput(
                attrs={
                    'id': 'ConfPassCl',
                    'placeholder': 'Ingrese la contraseña de nuevo'
                }
            ),

            'accept_terms': CheckboxInput(
                attrs={
                    'id': 'agreeTerms',
                    'name': 'terms',
                    'value': 'agree'
                }
            )


        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error en forms'] = str(e)
        return data