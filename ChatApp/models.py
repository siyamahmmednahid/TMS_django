from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Chat(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message