# Generated by Django 4.1.3 on 2023-01-04 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmailApp', '0010_rename_deleted_email_blindcarboncopydelete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='Sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]