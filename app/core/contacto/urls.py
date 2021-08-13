from django.urls import path
from core.contacto.views import needle_cont, ContactView

    # Esta es la url de CONTACTO

urlpatterns = [
    path('', ContactView.as_view(), name="contacto"),
    #path('', ContactView.as_view(), name='contact_developers'),
]