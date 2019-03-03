from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=50, default='')
    task_start_time = models.BigIntegerField(default=0)
    task_end_time = models.BigIntegerField(default=0)

    def __str__(self):
        return self.task_name


class AddTask(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.category


class Code(models.Model):
    code = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
