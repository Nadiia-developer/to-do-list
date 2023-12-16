from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-datetime_created", "-is_done"]

    def __str__(self):
        return (
            f" Task: {self.content}, "
            f"Created date: {self.datetime_created}, "
            f"Deadline: {self.deadline}, "
            f"Done: {self.is_done}, "
            f"Tags: {','.join(tag.name for tag in self.tags.all())}"
        )
