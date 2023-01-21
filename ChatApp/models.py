from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return f"{self.user1} and {self.user2}"



class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='conversation')
    Message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.conversation} - {self.timestamp}"