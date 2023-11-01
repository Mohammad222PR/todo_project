from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login", views.LoginUserView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("signup", views.SingUp.as_view(), name="signup"),
]