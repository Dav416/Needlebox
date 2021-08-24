from django.views.generic import TemplateView
from django.urls import reverse_lazy


# Create your views here.
# Formulario para modificar información de cuenta
class AyudaTemplateView(TemplateView):
    template_name = 'ayuda.html'
    success_url = reverse_lazy('perfil')

"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formP'] = ModificPerfilForm
        return context
"""