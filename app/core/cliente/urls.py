from django.urls import path
from core.cliente.views import NeedleCliente, NeedleNuevoCliente, NeedleNuevoCliente2,NeedleEditCliente,\
    NeedleVistaInfoAdicional

# Este es el url de clientes


urlpatterns = [
    path('clt/', NeedleCliente.as_view(), name="cliente"),
    path('nclient/', NeedleNuevoCliente.as_view(), name="cliente1"),
    path('nclient2/', NeedleNuevoCliente2.as_view(), name="cliente2"),
    path('editclient/', NeedleEditCliente.as_view(), name="cliente3"),
    path('infoadcl/', NeedleVistaInfoAdicional.as_view(), name="cliente4")
]