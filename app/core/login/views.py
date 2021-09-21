import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.forms import SetPasswordForm
from django.template.loader import render_to_string
import config.settings as setting
from config import settings

from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, JsonResponse

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from core.login.forms import ResetPasswordForm, ChangePasswordForm
from core.user.models import User


# Create your views here.

# Vista de Login
class NeedleLoginView(LoginView):
    template_name = 'loginprincipal.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# -------- VISTAS PARA RESTABLECER CONTRASEÑA ------------

# Envio de correo para recuperar contraseña
class NeedleRecpass(FormView):
    form_class = ResetPasswordForm
    template_name = 'recpass1.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, user):
        data = {}
        try:
            url = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
            user.token = uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email_to = user.email
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = 'Reseteo de contraseña'

            content = render_to_string('send_email.html', {
                'user': user,
                'link_resetpwd': 'http://{}/login/changepassword/{}/'.format(url, str(user.token)),
                'link_home': 'http://{}/{}/'.format(url, 'index')  # Distinto al video para que funcionara
            })
            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                email_to,
                                mensaje.as_string())
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)  # self.get_form()
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_pwd(user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        context['list_url'] = settings.LOGIN_URL
        return context


# Formulario despues del correo para cambio de contraseña
class ChangePasswordView(FormView):
    model = User
    form_class = ChangePasswordForm
    template_name = 'loginrecpass.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']
        if User.objects.filter(token=token).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect('/')  # se usó aquí la ruta sugerida en el video

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                user = User.objects.get(token=self.kwargs['token'])
                user.set_password(request.POST['password'])
                user.token = uuid.uuid4()
                user.save()
                print(request.POST['password'])
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        context['list_url'] = settings.LOGIN_URL
        return context