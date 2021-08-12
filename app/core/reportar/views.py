#from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from core.reportar.forms import ReportForm
from core.reportar.models import Reportfail
from django.urls import reverse_lazy
# Create your views here.

class needle_reperror(TemplateView):
    template_name = '../templates/reportar_error.html'

#METODO GET
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = Reportfail.objects.all()
        return context
"""

class ReportView(CreateView):
    model = Reportfail
    form_class = ReportForm
    template_name = 'reportar_error.html'
    success_url = reverse_lazy('reportar')