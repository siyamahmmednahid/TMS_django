from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Sender_set')
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receiver_set')
    Message = models.TextField()
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Sender.username + ' - ' + self.Receiver.username
