from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Email(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', blank=True, null=True)
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', blank=True, null=True)
    CarbonCopy = models.ManyToManyField(User, related_name='carboncopy', blank=True)
    BlindCarbonCopy = models.ManyToManyField(User, related_name='blindcarboncopy', blank=True)
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
    SenderLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    ReceiverLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    CarbonCopyLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')
    BlindCarbonCopyLabel = models.CharField(max_length=10, choices=Label_Choices, default='None')

    SenderDraft = models.BooleanField(default=False)
    ReceiverDraft = models.BooleanField(default=False)
    CarbonCopyDraft = models.BooleanField(default=False)
    BlindCarbonCopyDraft = models.BooleanField(default=False)

    SenderImportant = models.BooleanField(default=False)
    ReceiverImportant = models.BooleanField(default=False)
    CarbonCopyImportant = models.BooleanField(default=False)
    BlindCarbonCopyImportant = models.BooleanField(default=False)

    ReceiverRead = models.BooleanField(default=False)
    CarbonCopyRead = models.BooleanField(default=False)
    BlindCarbonCopyRead = models.BooleanField(default=False)

    SenderTrash = models.BooleanField(default=False)
    ReceiverTrash = models.BooleanField(default=False)
    CarbonCopyTrash = models.BooleanField(default=False)
    BlindCarbonCopyTrash = models.BooleanField(default=False)

    SenderDelete = models.BooleanField(default=False)
    ReceiverDelete = models.BooleanField(default=False)
    CarbonCopyDelete = models.BooleanField(default=False)
    BlindCarbonCopyDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject