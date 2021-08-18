from django.urls import path
from core.insumos.views import NeedleInsu, RegInsumoCreateView, RegProveedorCreateView, EditInsumoUpdateView, \
    EditProveedorUpdateView, ListProveedoresView, ListInsumosView, BorrarInsumoDeleteView, BorrarProveedorDeleteView

# Este es el url de insumos


urlpatterns = [
    path('opciones/', NeedleInsu.as_view(), name="insumos"),

    path('lista_proveedores/', ListProveedoresView.as_view(), name="lista_proveedores"),
    path('lista_insumos/', ListInsumosView.as_view(), name="lista_insumos"),

    path('nuevo_insumo/', RegInsumoCreateView.as_view(), name="registrar_insumo"),
    path('nuevo_proveedor/', RegProveedorCreateView.as_view(), name="registrar_proveedor"),

    path('editar_insumo/<int:pk>/', EditInsumoUpdateView.as_view(), name="editar_insumo"),
    path('editar_proveedor/<int:pk>/', EditProveedorUpdateView.as_view(), name="editar_proveedor"),

    path('delete_insumo/<int:pk>/', BorrarInsumoDeleteView.as_view(), name="borrar_insumo"),
    path('delete_proveedor/<int:pk>/', BorrarProveedorDeleteView.as_view(), name="borrar_proveedor"),
]
