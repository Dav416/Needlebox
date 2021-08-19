#from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from core.contacto.forms import ContactForm
from core.contacto.models import ContactUs
from django.urls import reverse_lazy
#Emails
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

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

#Envio de emails
def contacto(request):
    if request.method=="POST":

        name=request.POST['Nombre']

        message=request.POST['Mensaje'] + ' ' + request.POST['Email']

        email_from=settings.EMAIL_HOST_USER

        recipient_list=['needlebox.proyect@gmail.com']

        subject=request.POST['Asunto']

        send_mail(name,message, email_from, recipient_list, subject, fail_silently=False)

        print('El correo se ha enviado')

    return render(request, 'contacto.html')


