from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class NeedleIndex(TemplateView):
    template_name = '../templates/index.html'


"""
Como pasa con la vista de la app 'perfil', esta clase colo se limita ausa el modelo TemplateView como 
parametro para poder recibir mediante la variable predicifina template_name, la plantilla que le corresponde.
Con solo esto y con configurar la url que corresponde a esta vista-clase, es suficiente para que se pueda ver 
la pagina al correr el servidor.  
"""

