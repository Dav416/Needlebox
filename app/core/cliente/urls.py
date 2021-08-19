from django.urls import path
from core.cliente.views import NeedleCliente, NeedleNuevoCliente, NeedleEditCliente

# Este es el url de clientes


urlpatterns = [
    path('clt/', NeedleCliente.as_view(), name="cliente"),
    path('nclient/', NeedleNuevoCliente.as_view(), name="cliente1"),
    path('editclient/', NeedleEditCliente.as_view(), name="cliente3"),
]