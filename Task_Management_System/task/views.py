from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm
from category.models import TaskCategory

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.categories.set(form.cleaned_data['categories'])  # Assign selected categories
            task.save()
        return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
