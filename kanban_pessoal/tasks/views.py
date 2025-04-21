from django.shortcuts import render
from .models import Task

def kanban(request):
    return render(request, 'tasks/kanban.html', {
        'todo_tasks': Task.objects.filter(status='todo'),
        'done_tasks': Task.objects.filter(status='done'),
    })