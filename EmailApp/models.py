from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Email(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', blank=False)
    Receiver = models.ManyToManyField(User, related_name='receiver', blank=True)
    Cc = models.ManyToManyField(User, related_name='carboncopy', blank=True)
    Bcc = models.ManyToManyField(User, related_name='blindcarboncopy', blank=True)
    Subject = models.CharField(max_length=100, blank=True)
    Body = models.TextField(blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Draft = models.BooleanField(default=False)
    Label_Choices = (
        ('None', 'None'),
        ('Personal', 'Personal'),
        ('Important', 'Important'),
        ('Private', 'Private'),
        ('Company', 'Company'),
    )
    SenderLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    ReceiverLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    CcLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    BccLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')

    SenderImportant = models.BooleanField(default=False)
    ReceiverImportant = models.BooleanField(default=False)
    CcImportant = models.BooleanField(default=False)
    BccImportant = models.BooleanField(default=False)

    ReceiverRead = models.BooleanField(default=False)
    CcRead = models.BooleanField(default=False)
    BccRead = models.BooleanField(default=False)

    SenderTrash = models.BooleanField(default=False)
    ReceiverTrash = models.BooleanField(default=False)
    CcTrash = models.BooleanField(default=False)
    BccTrash = models.BooleanField(default=False)

    SenderDelete = models.BooleanField(default=False)
    ReceiverDelete = models.BooleanField(default=False)
    CcDelete = models.BooleanField(default=False)
    BccDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject