from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create', views.CreateTodoView.as_view(), name='todo_create_view'),
    path('tasks/done/<int:pk>', views.CompleteTaskView.as_view(), name='done'),
    path('tasks/update/<int:pk>', views.TaskUpdate.as_view(), name='update_view'),
    path('tasks/delete/<int:pk>', views.DeleteTodoView.as_view(), name='delete_view'),
    path('tasks/undone/<int:pk>', views.UnCompleteTaskView.as_view(), name='un_done'),
]
