# Generated by Django 4.1.3 on 2022-12-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0024_remove_personalinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachinginfo',
            name='Credit',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='teachinginfo',
            name='Semester',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
