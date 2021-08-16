from django.urls import path
from core.reportar.views import needle_reperror, ReportView



urlpatterns = [
    path('', ReportView.as_view(), name="reportar"),
    #path('', ReportView.as_view(), name='report_fail'),
]

