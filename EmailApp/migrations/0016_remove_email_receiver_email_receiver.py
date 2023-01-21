# Generated by Django 4.1.3 on 2023-01-20 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmailApp', '0015_alter_email_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='Receiver',
        ),
        migrations.AddField(
            model_name='email',
            name='Receiver',
            field=models.ManyToManyField(blank=True, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
