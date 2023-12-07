from django.urls import path, include
from . import views

from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login", views.LoginUserView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("signup", views.SingUp.as_view(), name="signup"),
    path('api/v1/', include('accounts.api.v1.urls', namespace='accounts-api-v1'))
]