from django.urls import path


from .views import (
    TagListView,
    TagAddView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    update_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/completed/",
        lambda request, pk: update_task_status(request, pk, is_done=True),
        name="task-completed",
    ),
    path(
        "tasks/<int:pk>/undo/",
        lambda request, pk: update_task_status(request, pk, is_done=False),
        name="undo-completed",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagAddView.as_view(), name="tag-add"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "to_do"
