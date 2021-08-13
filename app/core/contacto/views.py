#from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from core.contacto.forms import ContactForm
from core.contacto.models import ContactUs
from django.urls import reverse_lazy
# Create your views here.

class needle_cont(TemplateView):
    template_name = '../templates/contacto.html'

#METODO GET
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list1'] = ContactUs.objects.all()
        return context
"""
class ContactView(CreateView):
    model = ContactUs
    form_class = ContactForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('contacto')


