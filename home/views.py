from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from home.models import Todo


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')


class CreateTodoView(LoginRequiredMixin, CreateView):
    template_name = 'home/index.html'
    model = Todo
    fields = ["title"]
    success_url = reverse_lazy('home:todo_create_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(CreateTodoView, self).get_context_data(**kwargs)
        context['tasks'] = Todo.objects.all()
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'home/update_task.html'
    model = Todo
    fields = ['title']
    success_url = reverse_lazy('home:todo_create_view')


class CompleteTaskView(View):
    def get(self, request, pk):
        task = Todo.objects.get(id=pk)
        task.complete = True
        task.save()
        return redirect('home:todo_create_view')


class UnCompleteTaskView(View):
    def get(self, request, pk):
        task = Todo.objects.get(id=pk)
        task.complete = False
        task.save()
        return redirect('home:todo_create_view')


# class DeleteTodoView(LoginRequiredMixin, DeleteView):
#     model = Todo
#     context_object_name = "task"
#     success_url = reverse_lazy("home:todo_create_view")
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return self.model.objects.filter(user=self.request.user)

class DeleteTodoView(LoginRequiredMixin, View):
    def get(self, request, pk):
        todo = Todo.objects.get(id=pk)
        if todo.user.id == request.user.id:
            todo.delete()
            return redirect('home:todo_create_view')
