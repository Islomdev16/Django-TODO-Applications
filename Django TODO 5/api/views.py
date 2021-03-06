from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from todo_list.models import Task
from django.http import HttpResponseRedirect

# Create your views here.

@api_view(["GET"])
def getTodos(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getTodo(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def create_todo(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["PUT", "POST"])
def update_todo(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo(request, pk):
    # task = Task.objects.get(id=pk)
    if Task.objects.get(id=pk) is None:
        return HttpResponseRedirect("/")
    else:
        task.delete()
        task_id = task[0]
        return Response(f"{task_id} is deleted successfully !")

