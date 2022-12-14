# Generated by Django 4.1.3 on 2022-11-24 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver_set', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
