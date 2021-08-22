from django.urls import path
from core.login.views import NeedleLogin, NeedleRegis, NeedleRecpass

# Este es el url de clientes


urlpatterns = [
    # path('inilog/', NeedleLogin.as_view(), name="login1"),
    path('regprv/', NeedleRegis.as_view(), name="login2"),
    path('reccontr/', NeedleRecpass.as_view(), name="login3"),
]