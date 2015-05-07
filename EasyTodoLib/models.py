from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.DateField()
    done = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
