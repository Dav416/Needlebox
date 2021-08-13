from django.urls import path
from core.insumos.views import NeedleInsu, RegInsumoCreateView, RegProveedorCreateView, EditInsumoUpdateView, \
    EditProveedorUpdateView, ListProveedoresView, ListInsumosView

# Este es el url de index


urlpatterns = [
    path('opciones/', NeedleInsu.as_view(), name="insumos"),

    path('lista_proveedores/', ListProveedoresView.as_view(), name="lista_proveedores"),
    path('lista_insumos/', ListInsumosView.as_view(), name="lista_insumos"),

    path('nuevo_insumo/', RegInsumoCreateView.as_view(), name="registrar_insumo"),
    path('nuevo_proveedor/', RegProveedorCreateView.as_view(), name="registrar_proveedor"),

    path('editar_insumo/<int:pk>/', EditInsumoUpdateView.as_view(), name="editar_insumo"),
    path('editar_proveedor/<int:pk>/', EditProveedorUpdateView.as_view(), name="editar_proveedor"),
]
