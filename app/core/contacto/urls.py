from django.urls import path
from core.contacto.views import needle_cont

    # Esta es la url de CONTACTO

urlpatterns = [
    path('contactar/', needle_cont.as_view(), name="contacto"),
]