from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .tasks import Task, clean_up_completed_tasks
from home.models import Todo


# Create your views here.


class HomeView(View):
    """
    This line for return home page
    """

    def get(self, request):
        return render(request, "home/index.html")


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    This is the code to create a newer task in your daily list.
    """

    template_name = "home/index.html"
    model = Todo
    fields = ["title"]
    success_url = reverse_lazy("home:todo_create_view")

    def form_valid(self, form):
        """
        This section is for validating the form that we send
        """
        form.instance.user = self.request.user
        form.save()
        return redirect("home:todo_create_view")

    def get_context_data(self, **kwargs):
        """
        This section is for getting the list of tasks that we entered in our daily list
        """
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context["tasks"] = Todo.objects.all()
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    This is the code to update a task in your daily list
    """

    template_name = "home/update_task.html"
    model = Todo
    fields = ["title"]
    success_url = reverse_lazy("home:todo_create_view")


class TaskCompleteView(View):
    """
    This code is to check if this task is done.
    If it is clicked when it is done and the value was already done,
    it will set its value to false, but otherwise it will set its value to true.
    """

    def get(self, request, pk):
        task = Todo.objects.get(id=pk)
        if task.complete == True:
            task.complete == False
            task.save()
        else:
            task.complete == True
            task.save()
        return redirect("home:todo_create_view")


class TaskDeleteView(LoginRequiredMixin, View):
    """
    This is the code to delete a task in your daily list
    """

    def get(self, request, pk):
        todo = Todo.objects.get(id=pk)
        if todo.user.id == request.user.id:
            todo.delete()
            return redirect("home:todo_create_view")


class TaskView(View):
    def get(self, request, *args, **kwargs):
        Task.delay()
        return HttpResponse("<h1>Task d</h1>")


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
            return HttpResponse("<h1>Task d</h1>")

    
    def post(self, request, *args, **kwargs):
        clean_up_completed_tasks.delay()
        return HttpResponse("<h1>Taskdd d</h1>")


