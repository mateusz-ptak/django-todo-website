from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=20, null=False)
    message = models.CharField(max_length=100, null=False)
    deadline = models.DateField()