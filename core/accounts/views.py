from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView


# Create your views here.


class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home:home")


class SingUp(FormView):
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SingUp, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home:home")
        return super(SingUp, self).get(*args, **kwargs)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home:home")
