from django.db import models
from django.conf import settings

# Create your models here.

class Todolist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.todo_item}: {self.completed}"