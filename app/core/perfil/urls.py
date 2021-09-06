from django.urls import path
from core.perfil.views import UserUpdateView, UserDeleteView, UserChangePasswordView

# este es el url de perfil


urlpatterns = [
      path('editperfil/', UserUpdateView.as_view(), name="perfil"),
      path('deleteperfil/', UserDeleteView.as_view(), name="borrar_perfil"),
      path('changepassword/', UserChangePasswordView.as_view(), name="cambiar_contraseña"),
]
