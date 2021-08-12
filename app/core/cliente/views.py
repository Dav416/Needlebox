from django.views.generic import TemplateView, CreateView
from core.cliente.models import InfoClient, InfoGeneClient
from core.cliente.forms import InfoClientForm
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
class NeedleCliente(TemplateView):
    template_name = '../templates/clientes.html'

class NeedleNuevoCliente(CreateView):
    model = InfoClient
    form_class = InfoClientForm
    template_name = 'clientesnuevousu.html'
    success_url = reverse_lazy('cliente2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InfoClient.objects.all()
        context['form1'] = InfoClientForm
        return context

class NeedleNuevoCliente2(TemplateView):
    template_name = '../templates/clientesnuevousu2.html'

class NeedleEditCliente(TemplateView):
    template_name = '../templates/clientesedit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InfoClient.objects.all()
        context['form1'] = InfoClientForm
        return context




