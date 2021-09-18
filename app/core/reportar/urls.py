from django.urls import path
from core.reportar.views import ReportView

# Esta es la url de reportar

urlpatterns = [
    path('', ReportView.as_view(), name="reportar"),
    #path('', ReportView.as_view(), name='report_fail'),
]

#FALTA METODO GET