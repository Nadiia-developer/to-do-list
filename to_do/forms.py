from django import forms
from django.forms.widgets import DateTimeInput

from .models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
        widgets = {"deadline": DateTimeInput(attrs={"type": "datetime-local", "format": "%Y-%m-%dT%H:%M:"})}
