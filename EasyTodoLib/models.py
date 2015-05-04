from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.DateField()
    doneInPercent = models.DecimalField(max_digits=20, decimal_places=0)