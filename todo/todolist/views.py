from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Todolist
from .serializers import TodolistSerializer

# Create your views here.

def view_name(request):
    return render(request, 'homepage.html', {})

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    permission_class = [IsAuthenticated]
    
    def get_queryset(self):
        todolist = Todolist.objects.filter(user=self.request.user)
        return todolist
    
    def perform_create(self, serializer):
        # Set the user to the current authenticated user during creation
        serializer.save(user=self.request.user)