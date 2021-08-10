from django.urls import path
from core.perfil.views import ModPerfilCreateView

# este es el url de perfil


urlpatterns = [
    # path('perfil/', NeedlePerfil.as_view(), name="perfil"),
    path('perfil/', ModPerfilCreateView.as_view(), name="perfil"),
]
