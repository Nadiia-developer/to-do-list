from django.contrib import admin

from .models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "datetime_created",
        "deadline",
        "is_done"
    )
    list_filter = ("is_done", "tags")
    search_fields = ("content", "tags__name")


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
