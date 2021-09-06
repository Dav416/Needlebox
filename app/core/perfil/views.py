from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from core.user.models import User
from core.user.forms import *


# Create your views here.
# Formulario para modificar información de cuenta

# -------------Editar usuario--------------
class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'perfil.html'
    success_url = reverse_lazy('perfil')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG PROVEEDORES'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


# -------------Editar contraseña--------------
class UserChangePasswordView(UpdateView):
    model = User
    form_class = UserUpdatePasswordForm
    template_name = 'formchangepassword.html'
    success_url = reverse_lazy('perfil')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
                update_session_auth_hash(request, form.user)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['ERROR EN POST REG PROVEEDORES'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


# -------------Editar contraseña--------------
'''
class UserChangePasswordView(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'formchangepassword.html'
    success_url = reverse_lazy('perfil')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        form.fields['old_password'].widget.attrs['placeholder'] = 'Ingrese su contraseña actual'
        form.fields['new_password1'].widget.attrs['placeholder'] = 'Ingrese su nueva contraseña'
        form.fields['new_password2'].widget.attrs['placeholder'] = 'Repita su contraseña'
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

'''


# ----------------- BORRAR USUARIO ------------------------
class UserDeleteView(DeleteView):
    model = User
    template_name = 'BorrarPerfil.html'
    success_url = reverse_lazy('login1')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = self.success_url
        return context





"""
MÉTODO DISPATCH 
        def dispatch(self, request, *args, **kwargs):
            if request.method == 'GET':
                return redirect('perfil')
            return super().dispatch(request, *args, **kwargs)
"""

"""
Aunque se han creado un entidad/modelo/tabla con sus respectivo atributos o campos (se peude verificar
en los views de esta app, los mismos no han sido pasados aquí debido a qué no hay una tabla en sentido estricto
donde mostrar ese contenido. El formulario disponible en perfil está es destinado a edirar la información
de registro, de modo que cada usuario solo su vería una parte su 'unica e irrepetible' información, en la 
pestaña 'información personal' por ello aquí no se hace más que pasar la plantilla a la url como una vista.
"""