from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=50, default='')
    task_start_time = models.BigIntegerField(default=0)
    task_end_time = models.BigIntegerField(default=0)

    def __str__(self):
        return self.task_name


class AddTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.user.username
