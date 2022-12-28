from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Email(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    CarbonCopy = models.ManyToManyField(User, related_name='carboncopy')
    BlindCarbonCopy = models.ManyToManyField(User, related_name='blindcarboncopy')
    Subject = models.CharField(max_length=100)
    Body = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Label_Choices = (
        ('None', 'None'),
        ('Personal', 'Personal'),
        ('Important', 'Important'),
        ('Private', 'Private'),
        ('Company', 'Company'),
    )
    Label = models.CharField(max_length=10, choices=Label_Choices, default='None')
    Draft = models.BooleanField(default=False)
    Important = models.BooleanField(default=False)
    Read = models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject