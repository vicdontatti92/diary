from django.db import models


class TaskItem(models.Model):
    task_name = models.CharField(max_length=30)
    task_discription = models.CharField(max_length=1400)
