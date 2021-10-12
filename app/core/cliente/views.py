from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from core.cliente.models import InfoClient
from core.cliente.forms import InfoClientForm
from django.shortcuts import render
from django.urls import reverse_lazy


# Vista 1 / Página de redirección a las subfunciones del módulo
class NeedleCliente(TemplateView):
    template_name = '../templates/clientes.html'


# Vista 2 / Formulario de registro
class NeedleNuevoCliente(CreateView):
    model = InfoClient
    form_class = InfoClientForm
    template_name = 'clientesnuevousu.html'
    success_url = reverse_lazy('cliente3')

    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
            data['ERROR EN POST CLIENTES'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('cliente3')
        return context



# Vista 4 / Tabla con los clientes
class NeedleEditCliente(ListView):
    model = InfoClient
    template_name = '../templates/clientesedit.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = InfoClient.objects.get(pk=request.POST['id']).clientetojson()
        except Exception as e:
            data['error en post lista clientes'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userid = self.request.user.id
        context['object_list1'] = InfoClient.objects.all().filter(user_creation_id=userid)
        context['list_url'] = reverse_lazy('cliente3')
        return context


#Edit de Clientes

class EditClientesUpdate(UpdateView):
    model = InfoClient
    form_class = InfoClientForm
    template_name = 'clientesnuevousu.html'
    success_url = reverse_lazy('cliente3')


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'ERROR post edit clientes: No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR POST EDIT CLIENTES'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('cliente3')
        return context

#Delete de Clientes

class BorrarClienteDel(DeleteView):
    model = InfoClient
    template_name = 'borrarclienteview.html'
    success_url = reverse_lazy('cliente3')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('cliente3')
        return context