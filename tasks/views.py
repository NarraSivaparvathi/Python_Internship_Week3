from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(
        request,
        'tasks/task_form.html',
        {'form': form, 'title': 'Add Task'}
    )


@login_required
def task_update(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/task_form.html',
        {'form': form, 'title': 'Edit Task'}
    )


@login_required
def task_delete(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')

    return render(
        request,
        'tasks/task_confirm_delete.html',
        {'task': task}
    )
