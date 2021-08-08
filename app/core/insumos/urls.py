from django.urls import path
from core.insumos.views import NeedleInsu, RegInsumoCreateView

# Este es el url de index


urlpatterns = [
    path('insumos/', NeedleInsu.as_view(), name="insumos"),
    path('', RegInsumoCreateView.as_view(), name="registrar_insumo"),
]