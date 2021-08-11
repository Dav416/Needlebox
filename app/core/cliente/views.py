from django.views.generic import TemplateView
from core.cliente.models import InfoClient, InfoGeneClient
from django.shortcuts import render


# Create your views here.
class NeedleCliente(TemplateView):
    template_name = '../templates/clientes.html'

class NeedleNuevoCliente(TemplateView):
    template_name = '../templates/clientesnuevousu.html'

class NeedleNuevoCliente2(TemplateView):
    template_name = '../templates/clientesnuevousu2.html'

class NeedleEditCliente(TemplateView):
    template_name = '../templates/clientesedit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InfoClient.objects.all()

        return context