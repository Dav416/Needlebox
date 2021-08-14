from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class NeedleLogin(TemplateView):
    template_name = 'loginprincipal.html'

class NeedleRegis(TemplateView):
    template_name = '../templates/loginregusu.html'

class NeedleRecpass(TemplateView):
    template_name = '../templates/loginrecpass.html'
