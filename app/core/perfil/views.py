from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from core.perfil.models import Profile
from core.perfil.forms import ModificPerfilForm
from django.urls import reverse_lazy


# Create your views here.
# Formulario para modificar información de cuenta
class ModPerfilCreateView(CreateView):
    model = Profile
    form_class = ModificPerfilForm
    template_name = 'perfil.html'
    success_url = reverse_lazy('perfil')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formP'] = ModificPerfilForm
        return context


"""
MÉTODO DISPATCH 
        def dispatch(self, request, *args, **kwargs):
            if request.method == 'GET':
                return redirect('perfil')
            return super().dispatch(request, *args, **kwargs)
"""

"""
Aunque se han creado un entidad/modelo/tabla con sus respectivo atributos o campos (se peude verificar
en los views de esta app, los mismos no han sido pasados aquí debido a qué no hay una tabla en sentido estricto
donde mostrar ese contenido. El formulario disponible en perfil está es destinado a edirar la información
de registro, de modo que cada usuario solo su vería una parte su 'unica e irrepetible' información, en la 
pestaña 'información personal' por ello aquí no se hace más que pasar la plantilla a la url como una vista.
"""