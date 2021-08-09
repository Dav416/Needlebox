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
                    'id': 'forminsumos',
                    'class': 'custom-select insu-selec-opt'
                }
            ),

            'apeCli': TextInput(
                attrs={
                    'id': 'insudescr',
                    'class': ' insu-tipo-desc',
                    'rows': '3',
                    'placeholder': 'Rojo, con flores, antirrayones, pequeño, etc.'
                }
            ),

            'telCli': NumberInput(
                attrs={
                    'id': 'Insuinvent',
                    'placeholder': 'Agotado, 4 metros, etc'
                }
            ),

            'celCli': NumberInput(
                attrs={
                    'id': 'insucost',

                    'placeholder': '$'
                }
            ),

            'e_mailCli': EmailInput(
                attrs={
                    'id': 'insu-unid',
                    'placeholder': 'Cm, kg, unidad, etc.'
                }
            ),

            'dirCli': TextInput(
                attrs={
                    'id': 'insu-unid',
                    'placeholder': 'Cm, kg, unidad, etc.'
                }
            ),

            'imgCli': ImageInput(
                attrs={
                    'id': 'insu-unid',
                    'placeholder': 'Cm, kg, unidad, etc.'
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
                    'id': 'ProvName',
                    'placeholder': 'Local o persona',
                }
            ),

            'ver_ITC': TextInput(
                attrs={
                    'id': 'ProvMerca',
                    'class': 'insu-tipo-desc',
                    'rows': '6',
                    'placeholder': 'Adornos, telas, hilos u otros',
                }
            ),

            'revP_ITC': TextInput(
                attrs={
                    'id': 'ProvTel',
                    'placeholder': 'Número(s) telefónico(s) del proveedor',
                }
            ),

            'revIM_ITC': TextInput(
                attrs={
                    'id': 'ProvEmail',
                    'placeholder': 'E-mail del proveedor',
                }
            ),

            'tipoCli': Select(
                attrs={
                    'id': 'ProvDir',
                    'placeholder': 'Ubicación del proveedor',
                }
            ),

            'prenda': Select(
                attrs={
                    'id': 'ProvDir',
                    'placeholder': 'Ubicación del proveedor',
                }
            ),

            'estilCli': Select(
                attrs={
                    'id': 'ProvDir',
                    'placeholder': 'Ubicación del proveedor',
                }
            ),

            'medPag': Select(
                attrs={
                    'id': 'ProvDir',
                    'placeholder': 'Ubicación del proveedor',
                }
            )

        }