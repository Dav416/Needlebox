#from django.shortcuts import render
from django.views.generic import TemplateView
from core.reportar.models import Reportfail
# Create your views here.

class needle_reperror(TemplateView):
    template_name = '../templates/reportar_error.html'

#METODO GET

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = Reportfail.objects.all()
        return context