from django.views.generic import TemplateView, CreateView
from core.cliente.models import InfoClient
from core.cliente.forms import InfoClientForm
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
    success_url = reverse_lazy('cliente3')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG INSUMOS'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        
        #context['form'] = InfoClientForm
        context['list_url'] = reverse_lazy('cliente3')
        return context



# Vista 4 / Tabla con los clientes
class NeedleEditCliente(TemplateView):
    template_name = '../templates/clientesedit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = InfoClient.objects.all()
        context['form1'] = InfoClientForm
        return context




