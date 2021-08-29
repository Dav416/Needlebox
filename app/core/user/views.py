from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from core.user.models import User
from core.user.forms import UserRegForm, UserUpdateForm

# Create your views here.


# -------------registrar usuario--------------
class UserCreateView(CreateView):
    model = User
    form_class = UserRegForm
    template_name = 'loginregusu.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'registrar':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG PROVEEDORES'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'registrar'
        context['list_url'] = self.success_url
        return context