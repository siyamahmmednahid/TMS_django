# Generated by Django 4.1.3 on 2022-11-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0017_alter_personalinfo_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachinginfo',
            name='CourseCode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='teachinginfo',
            name='CourseTitle',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
