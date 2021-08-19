from django.forms import *

from core.cliente.models import InfoClient


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
            ),

            'infoTCli': Textarea(
                attrs={
                    'id': 'info_tec',
                    'rows': '3',
                    'placeholder': 'Notas, medidas, generalidades...'
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
# -----------------------------------------------------

