#from django.shortcuts import render
from django.views.generic import TemplateView
from core.contacto.models import ContactUs
# Create your views here.

class needle_cont(TemplateView):
    template_name = '../templates/contacto.html'

#METODO GET

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = ContactUs.objects.all()
        return context