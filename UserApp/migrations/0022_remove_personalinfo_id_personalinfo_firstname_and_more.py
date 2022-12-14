# Generated by Django 4.1.3 on 2022-12-19 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserApp', '0021_alter_awardandscholarshipinfo_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='FirstName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='LastName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
