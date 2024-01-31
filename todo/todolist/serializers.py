from rest_framework import serializers
from .models import Todolist

class TodolistSerializer(serializers.Serializer):
    class Meta:
        model = Todolist
        fields = '__all__'
