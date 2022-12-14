from django.db import models
from django.contrib.auth.models import User

# Create your models here.     
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Label_Choices = (
        ('None', 'Select Label'),
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('Family', 'Family'),
        ('Holiday', 'Holiday'),
        ('Other', 'Other'),
    )
    Label = models.CharField(max_length=10, choices=Label_Choices, default='None')
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    Guests = models.ManyToManyField(User, related_name='Guests_set', blank=True)
    WholeDay = models.BooleanField(default=False)
    EventURL = models.URLField(blank=True)
    Location = models.CharField(max_length=100, blank=True)
    Description = models.TextField(blank=True)

    def __str__(self):
        return self.Title + ' - ' + self.user.username