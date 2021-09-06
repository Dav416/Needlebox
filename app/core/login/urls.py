from django.urls import path
from core.login.views import NeedleRecpass, NeedleLoginView, LogoutView

# Este es el url de login


urlpatterns = [
    path('', NeedleLoginView.as_view(), name="login1"),
    path('reccontr/', NeedleRecpass.as_view(), name="login3"),
    path('logout/', LogoutView.as_view(next_page='login1'), name="logout"),
]