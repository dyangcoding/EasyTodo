from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.DateField()
    done = models.PositiveIntegerField(default=0)
