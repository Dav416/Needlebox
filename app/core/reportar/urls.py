from django.urls import path
from core.reportar.views import needle_reperror

# Esta es la url de PEDIDOS

urlpatterns = [
    path('report/', needle_reperror.as_view(), name="reportar"),
]

#FALTA METODO GET