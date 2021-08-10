from django.urls import path
from core.pedidos.views import needle_pedidos

# Esta es la url de PEDIDOS

urlpatterns = [
    path('ordenes/', needle_pedidos.as_view(), name="pedidos"),
]
