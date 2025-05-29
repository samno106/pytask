from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Task
from django.db.models import Q
from .forms import TaskForm
from django.views.decorators.http import require_http_methods
import time
# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    context = {"tasks": tasks, 'form':TaskForm()}
    return render(request, "views/home/index.html", context)


def search_task(request):
    
    time.sleep(0.5)
    query = request.GET.get('search', '')
    tasks = Task.objects.filter(Q(title__icontains=query)).order_by('-created_at')

    return render(request, 'views/home/components/task-list.html', {'tasks':tasks})

@require_http_methods(['POST'])
def create_task(request):
    time.sleep(0.5)
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=True)
        context = {'task':task}
        response = render(request,'views/home/components/task-item.html',context)
        response['HX-Trigger'] = 'success'
        return response
    return None


@require_http_methods(['DELETE'])
def task_delete(request, id):
    time.sleep(0.5)
    task = get_object_or_404(Task, id=id)
    task.delete()
    return HttpResponse("")

@require_http_methods(['PUT'])
def task_update_status(request,id):
    time.sleep(0.5)
    task = get_object_or_404(Task, id=id)
    task.status = "COMPLETED";
    task.save()
    context = {'task':task}
    response = render(request,'views/home/components/task-item.html',context)
    return response

@require_http_methods(['GET'])
def task_edit(request,id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(instance=task)
    context = {'task':task, 'form':form}

    return render(request, 'views/home/components/form-data.html',context)
    
@require_http_methods(['POST'])
def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=True)
        context = {'task':task}
        response = render(request,'views/home/components/task-item.html',context)
        response['HX-Trigger'] = 'success'
        return response
    return None

     