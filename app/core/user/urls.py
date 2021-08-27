"""
from django.urls import path
from core.user.views import UserCreateView

# Url registro user (registrar usarios)

urlpatterns = [
        path('regprv/', UserCreateView.as_view(), name="login2"),
]
"""