from django.shortcuts import redirect, render
from .models import Task


def home(request):
    '''
    TODO Home, show all tasks
    '''
    tasks = Task.objects.all().order_by('-date_created')
    return render(request, 'tasks/home.html', { 'tasks': tasks })


def done(request, pk):
    '''
    Mark task as done
    '''
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()
    return redirect('/')
