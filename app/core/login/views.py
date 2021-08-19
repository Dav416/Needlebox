from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render


# Create your views here.
class NeedleLogin(TemplateView):
    template_name = '../templates/loginprincipal.html'


class NeedleRegis(LoginView):
    template_name = '../templates/loginregusu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Regístrese por primera vez'
        return context

class NeedleRecpass(TemplateView):
    template_name = '../templates/loginrecpass.html'
