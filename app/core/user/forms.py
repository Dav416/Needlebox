# import numbers

from django.forms import *

from core.user.models import User


# ----------------REGISTRO DE USUARIOS---------------
class UserRegForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['required'] = True

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']
        widgets = {

            'first_name': TextInput(
                attrs={
                    'id': 'inputName',
                    'placeholder': 'Nombre completo',
                    'class': 'form-control',

                }
            ),


            'username': TextInput(
                attrs={
                    'id': 'inputUserName',
                    'placeholder': 'Nombre de usuario sin espacios',
                    'class': 'form-control',

                }
            ),

            'email': EmailInput(
                attrs={
                    'id': 'inputEmail',
                    'placeholder': 'Correo electrónico',
                    'class': 'form-control',


                }
            ),

            'password': PasswordInput(
                render_value=True,
                attrs={
                    'id': 'inputpass',
                    'minlength': '8',
                    'placeholder': 'Contraseña de mínimo 8 caracteres',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'step': '0',

                }
            ),

            'conf_password': PasswordInput(
                attrs={
                    'id': 'inputpass2',
                    'minlength': '8',
                    'placeholder': 'Repita su contraseña',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'step': '0',


                }
            ),

            'security_question': Select(
                attrs={
                    'id': 'Pregun-secur',
                    'class': 'custom-select selec-pre-opt form-control',

                }
            ),

            'security_answer': TextInput(
                attrs={
                    'id': 'Pregun-secur-res',
                    'class': 'form-control',
                    'placeholder': 'Respuesta a pregunta de seguridad',

                }
            ),

            'accept_terms': CheckboxInput(
                attrs={
                    'id': 'agreeTerms',
                    'name': 'terms',
                }
            ),

        }

    # validador de confirmación de contraseña
    def clean_password(self):
        if self.data['password'] != self.data['conf_password']:
            raise forms.ValidationError('Las contraseñas son distintas')
        return self.data['password']

    # check for digit
    """
    def number_password(self):
        nmrs = numbers
        if nmrs not in self.data['password']:
            raise forms.ValidationError('Incluya almenos un número')
        return self.data['password']
    """

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


# ----------------EDITAR INFO DE USUARIOS---------------
class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['required'] = True

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']
        widgets = {

            'first_name': TextInput(
                attrs={
                    'id': 'inputName',
                    'placeholder': 'Nombre completo',
                    'class': 'form-control',

                }
            ),


            'username': TextInput(
                attrs={
                    'id': 'inputUserName',
                    'placeholder': 'Nombre de usuario sin espacios',
                    'class': 'form-control',

                }
            ),

            'email': EmailInput(
                attrs={
                    'id': 'inputEmail',
                    'placeholder': 'Correo electrónico',
                    'class': 'form-control',


                }
            ),

            'password': PasswordInput(
                render_value=True,
                attrs={
                    'id': 'inputpass',
                    'minlength': '8',
                    'placeholder': 'Contraseña de mínimo 8 caracteres',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'step': '0',

                }
            ),

            'conf_password': PasswordInput(
                attrs={
                    'id': 'inputpass2',
                    'minlength': '8',
                    'placeholder': 'Repita su contraseña',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'step': '0',


                }
            ),

            'security_question': Select(
                attrs={
                    'id': 'Pregun-secur',
                    'class': 'custom-select selec-pre-opt form-control',

                }
            ),

            'security_answer': TextInput(
                attrs={
                    'id': 'Pregun-secur-res',
                    'class': 'form-control',
                    'placeholder': 'Respuesta a pregunta de seguridad',

                }
            ),

        }

    # validador de confirmación de contraseña
    def clean_password(self):
        if self.data['password'] != self.data['conf_password']:
            raise forms.ValidationError('Las contraseñas son distintas')
        return self.data['password']

    # check for digit
    """
    def number_password(self):
        nmrs = numbers
        if nmrs not in self.data['password']:
            raise forms.ValidationError('Incluya almenos un número')
        return self.data['password']
    """

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