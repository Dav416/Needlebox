#from django.shortcuts import render
from django.views.generic import  CreateView
from core.contacto.forms import ContactForm
from core.contacto.models import ContactUs
from django.urls import reverse_lazy
#Emails
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#METODO GET

class ContactView(CreateView):
    model = ContactUs
    form_class = ContactForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('contacto')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        email_from = settings.EMAIL_HOST_USER
        mensaje = 'ASUNTO: ' + form.cleaned_data.get(
            'cont_asunto') + '\n' + '\n' + 'Nombre de usuario: ' + form.cleaned_data.get(
            'cont_nombre') + '\n' + 'Correo del usuario: ' + form.cleaned_data.get(
            'correo_usu') + '\n' + '\n' + 'MENSAJE: ' + form.cleaned_data.get('cont_mensaje')
        send_mail(
            subject='Contacto: ' + form.cleaned_data.get('cont_asunto'),
            message=mensaje,
            from_email=email_from,
            recipient_list=["needlebox.proyect@gmail.com"],
        )
        return redirect(self.success_url + "?ok")








