#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from core.pedidos.models import Todopedido
# Create your views here.

#Modulo pedidos
class needle_pedidos(TemplateView):
    template_name = '../templates/pedidos.html'


#Tabla pedidos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = Todopedido.objects.all()
        return context


class pedidos_table(ListView):
    template_name = '../templates/tablapedidos.html'



