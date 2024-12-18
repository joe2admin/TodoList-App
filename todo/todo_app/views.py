from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

#list view
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/index.html', {'tasks': tasks})

#add view
def add_task(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'])
        task.save() 
        return redirect('task_list')

#delete view
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

#toggle completed
def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
