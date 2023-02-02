from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Assignee_set')
    DueDate = models.DateField()
    Priority_Choices = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    )
    Priority = models.CharField(max_length=10, choices=Priority_Choices, default='Low')
    Important = models.BooleanField(default=False)
    Completed = models.BooleanField(default=False)
    Description = models.TextField(blank=True)
    Comment = models.TextField(blank=True)
    TaskCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.Title + ' - ' + self.user.username