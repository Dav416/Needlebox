from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from core.login.forms import RegistrarUsuarioForm
from django.shortcuts import render


# Create your views here.
class NeedleLogin(LoginView):
    template_name = '../templates/loginprincipal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicie sesión'
        context['form1'] = RegistrarUsuarioForm
        return context


class NeedleRegis(TemplateView):
    template_name = '../templates/loginregusu.html'



class NeedleRecpass(TemplateView):
    template_name = '../templates/loginrecpass.html'
