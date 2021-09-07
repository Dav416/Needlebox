from django.urls import path
from core.login.views import NeedleRecpass, NeedleLoginView, LogoutView, ChangePasswordView

# Este es el url de login


urlpatterns = [
    path('', NeedleLoginView.as_view(), name="login1"),
    path('recpassword/', NeedleRecpass.as_view(), name="correo_rec_contraseña"),

    path('changepassword/<str:token>/', ChangePasswordView.as_view(), name="Cambiar_contraseña"),

    path('logout/', LogoutView.as_view(next_page='login1'), name="logout"),
]