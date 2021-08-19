from django.urls import path
from core.cliente.views import NeedleCliente, NeedleNuevoCliente, NeedleEditCliente, EditClientesUpdate

# Este es el url de clientes


urlpatterns = [
    path('clt/', NeedleCliente.as_view(), name="cliente"),
    path('nclient/', NeedleNuevoCliente.as_view(), name="cliente1"),
    path('editclient/', NeedleEditCliente.as_view(), name="cliente3"),
    path('update_list/<int:pk>/', EditClientesUpdate.as_view(), name="editar_cliente"),
]