from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # nececario para el decorador
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.pedidos.models import RegisPedido
from core.pedidos.forms import RegPedidoForm


# Create your views here.

# MENÚ PEDIDOS
class SelecOptionPedidos(TemplateView):
    template_name = 'pedidos.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# LISTA DE PEDIDOS
class ListPedidosView(ListView):
    model = RegisPedido
    template_name = 'tablapedidos.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = RegisPedido.objects.get(pk=request.POST['id']).pedidotojson()
        except Exception as e:
            data['error en post lista pedidos'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userid = self.request.user.id
        context['object_list'] = RegisPedido.objects.all().filter(user_creation_id=userid)
        context['list_url'] = reverse_lazy('lista_pedidos')
        return context


# REGISTRO para PEDIDOS
class RegPedidoCreateView(CreateView):
    model = RegisPedido
    form_class = RegPedidoForm
    template_name = 'formulariopedidos.html'
    success_url = reverse_lazy('lista_pedidos')

    @method_decorator(login_required)
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
            data['ERROR EN POST REG PEDIDOS'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('lista_pedidos')
        context['titulo'] = "Registrar pedidos"
        return context


# EDITAR para PEDIDOS
class EditPedidoUpdateView(UpdateView):
    model = RegisPedido
    form_class = RegPedidoForm
    template_name = 'formulariopedidos.html'
    success_url = reverse_lazy('lista_pedidos')

    @method_decorator(login_required)
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
                data['error'] = 'ERROR post edit pedidos: No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR POST EDIT PEDIDOS'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('lista_pedidos')
        context['titulo'] = "Editar pedidos"
        return context


# BORRAR para PEDIDOS
class BorrarPedidoDeleteView(DeleteView):
    model = RegisPedido
    template_name = 'BorrarPedido.html'
    success_url = reverse_lazy('lista_pedidos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('lista_pedidos')
        return context