#from django.shortcuts import render
from django.views.generic import  CreateView
from core.contacto.forms import ContactForm
from core.contacto.models import ContactUs
from django.urls import reverse_lazy
#Emails
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        email_from = settings.EMAIL_HOST_USER
        mensaje = 'Nombre de usuario: ' + form.cleaned_data.get('cont_nombre') + '\n' + 'Correo del usuario: ' + form.cleaned_data.get('correo_usu') + '\n' + '\n' + form.cleaned_data.get('cont_mensaje')


        send_mail(
            subject=form.cleaned_data.get('cont_asunto'),
            message= mensaje ,
            from_email=email_from,
            recipient_list=["needlebox.proyect@gmail.com"],

        )

        return HttpResponseRedirect(self.get_success_url())

#Libreria para la ventada de alerta (para mostrar que se envio el correo electronico)
#sweetalert2-9.10.0



#Envio de emails

"""

def contacto(request):
<<<<<<< HEAD
    if request.method =="POST":
=======
    if request.method == "POST":
>>>>>>> 16764ed586bdc0ec8c6aa6e02e42fd2d6da8285a

        name = request.POST['Nombre']

        message = request.POST['Mensaje'] + ' ' + request.POST['Email']

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ['needlebox.proyect@gmail.com']

        subject = request.POST['Asunto']

        send_mail(name, message, email_from, recipient_list, subject, fail_silently=False)

        print('El correo se ha enviado')

    return render(request, 'contacto.html')

"""





