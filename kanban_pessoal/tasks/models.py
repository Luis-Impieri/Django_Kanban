from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[
        ('todo', '📌 To-Do'),
        ('done', '✅ Done'),
    ])

    def __str__(self):
        return self.title