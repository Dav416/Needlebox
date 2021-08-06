from django.urls import path
from core.index.views import NeedleIndex

# Este es el url de index


urlpatterns = [
    path('index/', NeedleIndex.as_view(), name="index"),
]