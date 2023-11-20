from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.TaskCreateView.as_view(), name="todo_create_view"),
    path("tasks/done/<int:pk>", views.TaskUpdateView.as_view(), name="done"),
    path("tasks/update/<int:pk>", views.TaskUpdateView.as_view(), name="update_view"),
    path("tasks/delete/<int:pk>", views.TaskDeleteView.as_view(), name="delete_view"),
]
