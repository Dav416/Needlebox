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


from core.views import needle_cliente, needle_nuevocliente, needle_nuevocliente2, \
    needle_editcliente, needle_crono, needle_pedidos, needle_nosotros, needle_reperror, needle_ayuda, \
    needle_cont, needle_login, needle_regis, needle_recpass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('core.index.urls')),
    path('clientes/', needle_cliente),
    path('nclient/', needle_nuevocliente),
    path('nclient2/', needle_nuevocliente2),
    path('editclient/', needle_editcliente),
    path('cronograma/', needle_crono),
    path('pedidos/', include ('core.pedidos.urls')),
    path('insumos_proveedores/', include('core.insumos.urls')),
    path('cuenta/', include('core.perfil.urls')),
    path('nosotros/', needle_nosotros),
    path('error/', include('core.reportar.urls')),
    path('ayuda/', needle_ayuda),
    path('contactenos/', include('core.contacto.urls')),
    path('login/', needle_login),
    path('registro/', needle_regis),
    path('recuperar/', needle_recpass),

    # path('clientes2/', include('ruta.de.la.url.especificas.de.la.app')),
    # path('insu_insu/', ListInsuView.as_view(), name="lista_insumos"),
    # path('insu_prov/', ListProvView.as_view(), name="lista_Proveedores"),
]
