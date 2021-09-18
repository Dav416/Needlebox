#from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from core.reportar.forms import ReportForm
from core.reportar.models import Reportfail
from django.urls import reverse_lazy

#Emails
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class needle_reperror(TemplateView):
    template_name = '../templates/reportar_error.html'


class ReportView(CreateView):
    model = Reportfail
    form_class = ReportForm
    template_name = 'reportar_error.html'
    success_url = reverse_lazy('reportar')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        email_from = settings.EMAIL_HOST_USER
        mensaje = 'Nombre de usuario: ' + form.cleaned_data.get('error_nombre') + '\n' + 'Correo del usuario: ' \
                  + form.cleaned_data.get('correo_usu') + '\n' + '\n' + 'Error: ' + form.cleaned_data.get('tip_error') \
                  + '\n' + '\n' + form.cleaned_data.get('cont_mensaje')
        send_mail(
            subject='Reporte de error',
            message= mensaje,
            from_email=email_from,
            recipient_list=["needlebox.proyect@gmail.com"],
        )
        return HttpResponseRedirect(self.get_success_url())
#Falta enviar la opcion seleccionada del desplegable por correo electronico
#Falta anexar alerta de envio exitoso