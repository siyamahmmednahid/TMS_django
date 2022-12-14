from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Email(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    Subject = models.CharField(max_length=100)
    Body = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Subject