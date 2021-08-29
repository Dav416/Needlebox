from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


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







# Vista de Registro de usuario
class NeedleRegis(TemplateView):
    template_name = '../templates/loginregusu.html'


# Vista de Recuperar conraseña
class NeedleRecpass(TemplateView):
    template_name = '../templates/loginrecpass.html'
