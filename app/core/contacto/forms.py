from django.forms import *
from core.contacto.models import ContactUs

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'cont_nombre': TextInput(
                attrs={
                    'id': 'inputName',
                    'class': 'form-control',
                    'name': 'Nombre'
                }
                ),
            'correo_usu': EmailInput(
                attrs={
                    'id': 'inputEmail',
                    'class': 'form-control',
                    'name': 'Email'
                }
                ),
            'cont_asunto': TextInput(
                attrs={
                    'id': 'inputSubject',
                    'class': 'form-control',
                    'name': 'Asunto'
                }
                ),
            'cont_mensaje': Textarea(
                attrs={
                    'id': 'inputMessage',
                    'class': 'form-control',
                    'rows': '4',
                    'name': 'Mensaje'
                }
                )
        }