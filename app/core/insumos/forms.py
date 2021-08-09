from django.forms import *

from core.insumos.models import InsRegInsu, InsRegProv


# -------------------------------
class RegInsumoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = InsRegInsu
        fields = '__all__'
        widgets = {
            'tipo_insumo': Select(
                attrs={
                    'id': 'forminsumos',
                    'class': 'custom-select insu-selec-opt'
                }
            ),

            'especificacion_insumo': Textarea(
                attrs={
                    'id': 'insudescr',
                    'class': ' insu-tipo-desc',
                    'rows': '3',
                    'placeholder': 'Rojo, con flores, antirrayones, pequeño, etc.'
                }
            ),

            'estado_insumo': TextInput(
                attrs={
                    'id': 'Insuinvent',
                    # 'class': 'form-control', Borro las clases con solo from control, porque ya las intera la función
                    'placeholder': 'Agotado, 4 metros, etc'
                }
            ),

            'costxunid_insumo_costo': NumberInput(
                attrs={
                    'id': 'insucost',

                    'placeholder': '$'
                }
            ),

            'costxunid_insumo_unidad': TextInput(
                attrs={
                    'id': 'insu-unid',
                    'placeholder': 'Cm, kg, unidad, etc.'
                }
            )
        }
# -----------------------------------------------------


class RegProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = InsRegProv
        fields = '__all__'
        widgets = {
            'nombre_proveedor': TextInput(
                attrs={
                    'id': 'ProvName',
                    'placeholder': 'Local o persona',
                }
            ),

            'Insumos_proveedor': Textarea(
                attrs={
                    'id': 'ProvMerca',
                    'class': 'insu-tipo-desc',
                    'rows': '6',
                    'placeholder': 'Adornos, telas, hilos u otros',
                }
            ),

            'telefono_proveedor': TextInput(
                attrs={
                    'id': 'ProvTel',
                    'placeholder': 'Número(s) telefónico(s) del proveedor',
                }
            ),

            'correo_proveedor': EmailInput(
                attrs={
                    'id': 'ProvEmail',
                    'placeholder': 'E-mail del proveedor',
                }
            ),

            'ubicacion_proveedor': TextInput(
                attrs={
                    'id': 'ProvDir',
                    'placeholder': 'Ubicación del proveedor',
                }
            ),

        }