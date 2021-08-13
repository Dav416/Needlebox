from django.forms import *
from core.reportar.models import Reportfail

class ReportForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'campo-tab-err'

    class Meta:
        model = Reportfail
        fields = '__all__'
        widgets = {
            'error_nombre': TextInput(
                attrs={
                    'id': 'name',
                    'class': 'campo-tab-err',
                    'placeholder': 'Ingresa tu Nombre',
                }
                ),
            'correo_usu': EmailInput(
                attrs={
                    'id': 'email',
                    'class': 'campo-tab-err',
                    'placeholder': 'Email@hotmail.com'
                }
                ),
            'tip_error': Select(
                attrs={
                    'name': 'formulario_error',
                    'id': 'formulario_error',
                    'class': 'tabla_error campo-tab-err'
                }
                ),
            'cont_mensaje': Textarea(
                attrs={
                    'name': 'message',
                    'id': 'message',
                    'cols': '30',
                    'rows': '5',
                    'class': 'campo-tab-err'
                }
                )
        }