"""
from django.urls import path
from core.user.views import *

# Url registro user (registrar usarios)

urlpatterns = [
        path('regprv/', UserCreateView.as_view(), name="login2"),
        path('changepassword/', UserChangePasswordView.as_view(), name="cambiar_contraseña"),
]
"""