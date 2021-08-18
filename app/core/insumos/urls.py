from django.urls import path
from core.insumos.views import NeedleInsu, RegInsumoCreateView, RegProveedorCreateView, EditInsumoUpdateView

# Este es el url de index


urlpatterns = [
    path('insumos/', NeedleInsu.as_view(), name="insumos"),
    path('insu/', RegInsumoCreateView.as_view(), name="registrar_insumo"),
    path('prov/', RegProveedorCreateView.as_view(), name="registrar_proveedor"),
    path('editnsu/<int:pk>/', EditInsumoUpdateView.as_view(), name="editar_insumo"),
]
