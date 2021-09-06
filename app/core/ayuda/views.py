from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# Formulario para modificar información de cuenta
class AyudaTemplateView(TemplateView):
    template_name = 'ayuda.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formP'] = ModificPerfilForm
        return context
"""