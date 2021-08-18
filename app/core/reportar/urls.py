from django.urls import path
from core.reportar.views import needle_reperror, ReportView

# Esta es la url de PEDIDOS

urlpatterns = [
    path('', ReportView.as_view(), name="reportar"),
    #path('', ReportView.as_view(), name='report_fail'),
]

#FALTA METODO GET