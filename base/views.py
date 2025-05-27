from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.db.models import Q
from .forms import TaskForm
from django.views.decorators.http import require_http_methods
# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    context = {"tasks": tasks, 'form':TaskForm()}
    return render(request, "views/home/index.html", context)


def search_task(request):
    import time
    time.sleep(1)
    query = request.GET.get('search', '')
    tasks = Task.objects.filter(Q(title__icontains=query))

    return render(request, 'views/home/components/task-list.html', {'tasks':tasks})

@require_http_methods(['POST'])
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=True)
        context = {'task':task}
        response = render(request,'views/home/components/task-item.html',context)
        response['HX-Trigger'] = 'success'
        return response