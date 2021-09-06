from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class NosotrosTemplateView(TemplateView):
    template_name = 'nosotros.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)