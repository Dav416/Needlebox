from django.views.generic import TemplateView, CreateView
from core.cliente.models import InfoClient, InfoGeneClient
from core.cliente.forms import InfoClientForm, InfoGeneClientForm
from django.shortcuts import render
from django.urls import reverse_lazy


# Vista 1 / Página de redirección a las subfunciones del módulo
class NeedleCliente(TemplateView):
    template_name = '../templates/clientes.html'


# Vista 2 / Primer formulario de registro
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


# Vista 3 / Segundo formulario de registro - Info adicional
class NeedleNuevoCliente2(CreateView):
    model = InfoGeneClient
    form_class = InfoGeneClientForm
    template_name = 'clientesnuevousu2.html'
    success_url = reverse_lazy('cliente4')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list2'] = InfoGeneClient.objects.all()
        context['form2'] = InfoGeneClientForm
        return context


# Vista 4 / Tabla con los clientes
class NeedleEditCliente(TemplateView):
    template_name = '../templates/clientesedit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InfoClient.objects.all()
        context['form1'] = InfoClientForm
        return context


# Vista 5 / Lista con la información adicional de cada cliente según el formulario 2
class NeedleVistaInfoAdicional(TemplateView):
    template_name = '../templates/vistainfoadicional.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list2'] = InfoGeneClient.objects.all()
        context['form2'] = InfoGeneClientForm
        return context



