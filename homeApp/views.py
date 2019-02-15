from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Task, AddTask
from .serializers import TaskSerializer, AddTaskSerializer
from django.shortcuts import get_object_or_404


class TaskPostView(APIView):
    """
    This class used to task view and create
    """

    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class TaskDetailsViews(APIView):
    """
    This method used to task `retrieve`  `update` and `destroy`
    """

    def get(self, request, id):
        queryset = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(queryset).data
        return Response(serializer)

    def put(self, request, id):
        queryset = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(Task, id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddTaskView(APIView):
    """
    Add task view ManyToMany relation Task . Here this class use to task create and view
    """

    def get(self, request):
        queryset = AddTask.objects.all()
        serializer = AddTaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddTaskRetrieveView(APIView):
    """
    Here, server add new task `Details` `Update` and `Delete` function using prepare data
    """

    def get(self, request, id):
        queryset = get_object_or_404(AddTask, id=id)
        serializer = AddTaskSerializer(queryset).data
        return Response(serializer)

    def put(self, request, id):
        queryset = get_object_or_404(AddTask, id=id)
        serializer = AddTaskSerializer(queryset, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = get_object_or_404(AddTask, id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
