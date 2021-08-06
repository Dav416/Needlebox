from django.urls import path
from core.insumos.views import NeedleInsu

# Este es el url de index


urlpatterns = [
    path('insumos/', NeedleInsu.as_view(), name="insumos"),
]