# Generated by Django 4.1.3 on 2022-11-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0012_alter_personalinfo_nidnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='DateOfBirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='Nationality',
            field=models.CharField(max_length=20),
        ),
    ]
