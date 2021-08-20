from django.urls import path
from core.ayuda.views import AyudaTemplateView

# este es el url de perfil


urlpatterns = [
       path('ayuda_opciones/', AyudaTemplateView.as_view(), name="ayuda"),
]
