from django.views.generic import TemplateView


# Create your views here.

class NeedlePerfil(TemplateView):
    template_name = '../templates/perfil.html'


"""
Aunque se han creado un entidad/modelo/tabla con sus respectivo atributos o campos (se peude verificar
en los views de esta app, los mismos no han sido pasados aquí debido a qué no hay una tabla en sentido estricto
donde mostrar ese contenido. El formulario disponible en perfil está es destinado a edirar la información
de registro, de modo que cada usuario solo su vería una parte su 'unica e irrepetible' información, en la 
pestaña 'información personal' por ello aquí no se hace más que pasar la plantilla a la url como una vista.
"""

