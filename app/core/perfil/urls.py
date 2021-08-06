from django.urls import path
from core.perfil.views import NeedlePerfil

# este es el url de perfil


urlpatterns = [
    path('perfil/', NeedlePerfil.as_view(), name="perfil"),
]
