from django.forms import *

from core.cliente.models import InfoClient, InfoGeneClient


# -------------------------------
class InfoClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = InfoClient
        fields = '__all__'
        widgets = {
            'nomCli': TextInput(
                attrs={
                    'id': 'NuevCl',
                    'class': 'input-nuevclien'
                }
            ),

            'apeCli': TextInput(
                attrs={
                    'id': 'ApeNuevCl',
                    'class': 'input-nuevclien'
                }
            ),

            'telCli': NumberInput(
                attrs={
                    'id': 'TelNuevCl',
                    'class': 'input-nuevclien'
                }
            ),

            'celCli': NumberInput(
                attrs={
                    'id': 'CelNuevCl',
                    'class': 'input-nuevclien'
                }
            ),

            'e_mailCli': EmailInput(
                attrs={
                    'id': 'EmNuevCl',
                    'class': 'input-nuevclien'
                }
            ),

            'dirCli': TextInput(
                attrs={
                    'id': 'DirNuevCli',
                    'class': 'input-nuevclien'
                }
            )

        }
# -----------------------------------------------------


class InfoGeneClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = InfoGeneClient
        fields = '__all__'
        widgets = {
            'infoTCli': Textarea(
                attrs={
                    'id': 'info_tec',
                    'rows': '3',
                    'placeholder': 'Medidas y demás...'
                }
            ),

            'ver_ITC': TextInput(
                attrs={
                    'id': 'inputSuccess',
                    'class': 'form-control is-valid',
                    'placeholder': 'Ingrese observación ...'
                }
            ),

            'revP_ITC': TextInput(
                attrs={
                    'id': 'inputWarning',
                    'class': 'form-control is-warning',
                    'placeholder': 'Ingrese observación ...'
                }
            ),

            'revIM_ITC': TextInput(
                attrs={
                    'id': 'inputError',
                    'class': 'form-control is-invalid',
                    'placeholder': 'Ingrese observación ...'
                }
            ),

            'tipoCli': Select(
                attrs={
                    'id': 'LocCl',
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),

            'prenda': Select(
                attrs={
                    'id': 'PrendCl',
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),

            'estilCli': Select(
                attrs={
                    'id': 'estilo_cli',
                }
            ),

            'medPag': Select(
                attrs={
                    'id': 'mediopagoh',
                }
            )

        }