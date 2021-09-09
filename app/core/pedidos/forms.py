from django.forms import *
from django import forms
from core.pedidos.models import RegisPedido


# ---------------Para escoger fechas----------------
class DateInput(forms.DateInput):
    input_type = 'date'


# ----------------REGISTRO DE PEDIDOS---------------
class RegPedidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RegisPedido
        fields = '__all__'
        widgets = {
            'nombCli': TextInput(
                attrs={
                    'id': 'InputCliente',
                    'class': '',
                    'placeholder': 'Nombre completo del cliente',
                }
            ),

            'descriped': Textarea(
                attrs={
                    'id': 'inputTipoPedido',
                    'class': 'custom-select',
                    'placeholder': 'Detalles de elaboración o de otro tipo para el pedido',
                    'rows': '3',
                }
            ),

            'costoped': NumberInput(
                attrs={
                    'id': 'PedCosto',
                    'placeholder': '$'
                }
            ),

            'fecharec': DateInput(
                attrs={
                    'id': 'PedFechaRec',
                    'class': '',
                    'placeholder': 'Introduzca la fecha de recepción'
                }
            ),

            'fechaLiEn': DateInput(
                attrs={
                    'id': 'inputFechaLimEntrega',
                    'placeholder': 'Introduzca la fecha de entrega'
                }
            ),

            'medentr': Select(
                attrs={
                    'id': 'inputMedioEntrega',
                    'class': 'custom-select',
                    'placeholder': 'Servicio de correo, personal, etc.'
                }
            ),

            'DetailEntr': Textarea(
                attrs={
                    'id': 'inputLugarEntrega',
                    'placeholder': 'Lugar, hora y otros detalles de entrega del pedido',
                    'rows': '3',
                }
            ),

            'estped': Textarea(
                attrs={
                    'id': 'Estado_pedido',
                    'class': '',
                    'placeholder': 'Recepción, toma de medidas, diseño de molde, corte, estampado, finalizado, etc',
                    'rows': '3',
                }
            ),

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