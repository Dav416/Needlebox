from django.forms import *
from core.perfil.models import Profile


# -------------------------------
class ModificPerfilForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'nom_usu': TextInput(
                attrs={
                    'id': 'inputName',
                    'placeholder': 'Nombre de usuario',
                    'class': 'form-control'
                }
            ),

            'e_mail': EmailInput(
                attrs={
                    'id': 'inputEmail',
                    'placeholder': 'E-mail',
                    'class': 'form-control'
                }
            ),

            'password': PasswordInput(
                attrs={
                    'id': 'inputpass',
                    'minlength': '8',
                    'placeholder': 'Su contraseña debe tener mínimo 5 caracteres y 1 número',
                    'class': 'form-control',
                    'autocomplete': 'off',

                }
            ),

            'conf_password': PasswordInput(
                attrs={
                    'id': 'inputpass2',
                    'minlength': '8',
                    'placeholder': 'Repita su contrañea',
                    'class': 'form-control',
                    'autocomplete': 'off',

                }
            ),

            'show_password': CheckboxInput(
                attrs={
                    'id': 'ver-pass',
                    'name': 'see-pass-input',
                    'class': 'ver-pass-check',
                    'value': 'si'
                }
            ),


            'security_question': Select(
                attrs={
                    'id': 'Pregun-secur',
                    'class': 'custom-select selec-pre-opt form-control'
                }
            ),

            'security_answer': TextInput(
                attrs={
                    'id': 'Pregun-secur-res',
                    'class': 'form-control',
                    'placeholder': 'Respuesta a pregunta de seguridad'
                }
            ),

            'accept_terms': CheckboxInput(
                attrs={
                    'required': True,
                }
            ),



        }