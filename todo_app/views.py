from django.shortcuts import render
from .models import ToDo, ToDoList

def index(request):
    lists = ToDoList.objects.all()
    return render(request, 'todo_app/index.html', {'lists': lists})

def add_list(request):
    if request.method == "POST"
        title = request.POST['title']
        new_list = ToDoList(title=title)
        new_list.save()
        return redirect('index')
    return render(request, 'todo_app/add_list.html')

def add_task(request, list_id):
    task_list = ToDoList.objects.get(pk=list_id)
    if requet.method == "POST":
        task = request.POST['task']
        new_task = ToDo(task=task, task_list=task_list)
        new_task.save()
        return redirect('index')
    return render(request, 'todo_app/add_task.html', {'list':task_list})

def complete_task(request, task_id):
    task = ToDo.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')
