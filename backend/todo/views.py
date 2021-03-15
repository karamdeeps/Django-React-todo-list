from django.shortcuts import render
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
