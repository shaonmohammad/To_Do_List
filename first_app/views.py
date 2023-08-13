from django.shortcuts import render, redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel
# Create your views here.


def home(request):
    return render(request, './base.html')


def assign_tasks(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show_tasks')
    else:
        task = TaskForm()
    return render(request, './assign_tasks.html', {'form': task})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, './show_tasks.html', {'tasks': tasks})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_tasks')


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    tasks = TaskForm(instance=task)
    if request.method == "POST":
        tasks = TaskForm(request.POST, instance=task)
        if tasks.is_valid:
            tasks.save()
            return redirect('assign_tasks')
    else:
        tasks = TaskForm()
    return render(request, './assign_tasks.html', {'form': tasks})


def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.Status = True
    task.save()
    return redirect('completed_tasks')


def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(Status=True)
    return render(request, 'completed_tasks.html', {'tasks': completed_tasks})
