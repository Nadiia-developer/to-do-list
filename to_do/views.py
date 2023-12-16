from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


from .models import Tag
from .forms import Task, TaskForm


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:task-list")


def update_task_status(request, pk, is_done):
    task = get_object_or_404(Task, pk=pk)

    if task.is_done != is_done:
        task.is_done = is_done
        task.save()
    context = {"task": task}
    return render(request, "to_do/update_task_status.html", context=context)


def task_completed(request, pk):
    return update_task_status(request, pk, is_done=True)


def undo_completed(request, pk):
    return update_task_status(request, pk, is_done=False)


def tags(request):
    form = Tag
    return render(request, "to_do/tag_form.html", {"form": form})


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "to_do/tag_list.html"


class TagAddView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tag-list")
