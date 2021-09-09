from django.urls import path
from core.pedidos.views import *

# Este es el url de pedidos

urlpatterns = [
    path('opciones_pedidos/', SelecOptionPedidos.as_view(), name="pedidos"),

    path('lista_pedidos/', ListPedidosView.as_view(), name="lista_pedidos"),

    path('nuevo_pedido/', RegPedidoCreateView.as_view(), name="registrar_pedido"),

    path('editar_pedido/<int:pk>/', EditPedidoUpdateView.as_view(), name="editar_pedido"),

    path('delete_pedido/<int:pk>/', BorrarPedidoDeleteView.as_view(), name="borrar_pedido"),
]
