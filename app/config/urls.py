"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.nosotros.views import NosotrosTemplateView
from core.ayuda.views import AyudaTemplateView
from core.user.views import UserCreateView, UserChangePasswordView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('core.index.urls')),
    path('clientes/', include('core.cliente.urls')),
    path('pedidos/', include('core.pedidos.urls')),
    path('insumos_proveedores/', include('core.insumos.urls')),
    path('cuenta/', include('core.perfil.urls')),
    path('nosotros/', NosotrosTemplateView.as_view(), name="nosotros"),
    path('error/', include('core.reportar.urls')),
    path('ayuda/', AyudaTemplateView.as_view(), name="ayuda"),
    path('contactenos/', include('core.contacto.urls')),
    path('login/', include('core.login.urls')),
    path('reguser/', UserCreateView.as_view(), name="login2"),
    path('changepassword/', UserChangePasswordView.as_view(), name="cambiar_contraseña"),
    path('reportar/', include('core.reportar.urls')),
]