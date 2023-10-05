from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Todo(models.Model):
    task_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    task = models.CharField(max_length=200)
    
    def __str__(self):
        return self.task
    