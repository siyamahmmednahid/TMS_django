# Generated by Django 4.1.3 on 2023-01-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmailApp', '0004_alter_email_blindcarboncopy_alter_email_carboncopy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='Draft',
            field=models.BooleanField(default=False),
        ),
    ]